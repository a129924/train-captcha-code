from typing import Union

from torch import Tensor
from torch.autograd import Variable
from typing_extensions import Self, override

from .base import ModelBaseTrainer

__all__ = ["CNNModelTrainer"]


class CNNModelTrainer(ModelBaseTrainer):
    def calculate_loss_value(
        self,
        outputs: Tensor,
        labels: Tensor,
        requires_grad: bool = False,
    ) -> Tensor:
        """
        calculate_loss_value 計算train階段 predict label跟true label之間的相似度

        Args:
            outputs (Tensor): 多個train過model的值
            labels (Tensor): 多個true labels
            requires_grad (bool): 是否要重新計算剃度

        Returns:
            Tensor: 回傳相似度
        """
        from torch import zeros

        loss: Tensor = zeros(1, requires_grad=requires_grad)
        for i in range(labels.shape[1]):  # 對每個字符計算損失
            loss = loss + self.criterion(
                outputs[:, i, :], labels[:, i]
            )  # label每一個字的缺失值

        return loss

    @override
    def train(self, model_save_path: str, *, num_epochs: int) -> Self:
        best_loss: float = float("inf")  # 初始化最佳損失為無限大

        for epoch in range(1, num_epochs + 1):
            self.logger.info(msg=f"第{epoch}次訓練開始")

            running_loss: float = self.process_train_batch()
            epoch_loss = running_loss / len(self.train_loader)

            if epoch_loss < best_loss:
                from torch import save

                best_loss = epoch_loss
                save(self.model.state_dict(), model_save_path)

            self.logger.info(msg=f"第{epoch}次訓練結束, {running_loss = }")

        self.logger.info(msg="Finished Training")

        return self

    def process_train_batch(self) -> float:
        """
        process_train_batch 處理計算train階段每一次batch的loss值

        Returns:
            float: 當次batch的loss值
        """

        running_loss: float = 0.0
        for batch in self.train_loader:
            images = Variable(batch.image)
            labels = Variable(batch.label_index)

            self.optimizer.zero_grad()  # 清除梯度
            outputs = self.model(images)  # 前向傳播
            # 計算損失
            loss = self.calculate_loss_value(
                outputs=outputs, labels=labels, requires_grad=True
            )

            loss.backward()  # 反向傳播
            self.optimizer.step()  # 更新權重

            running_loss += loss.item()

        return running_loss

    def process_predict_batch(self) -> tuple[float, int, Union[int, float]]:
        from torch import max, no_grad

        val_loss = 0.0
        correct = 0
        total = 0

        self.model.eval()  # 確保模型處於評估模式

        with no_grad():  # 禁用梯度計算
            for batch in self.test_loader:
                val_images: Tensor = batch.image
                val_labels: Tensor = batch.label_index

                outputs = self.model(val_images)

                loss = self.calculate_loss_value(outputs=outputs, labels=val_labels)
                val_loss += loss.item()

                _, predicted = max(outputs, 2)  # 取得每個字符的預測結果

                correct += (predicted == val_labels).sum().item()
                total += val_labels.size(0) * val_labels.size(1)

        return val_loss, total, correct

    @override
    def validate(self, num_epochs: int) -> Self:
        for epoch in range(1, num_epochs + 1):
            self.logger.info(msg=f"第{epoch}次驗證開始")

            val_loss, total, correct = self.process_predict_batch()

            val_loss = val_loss / len(self.test_loader)
            accuracy = 100 * correct / total

            self.logger.info(
                msg=f"第{epoch}次驗證結束 Validation Loss: {val_loss}, Accuracy: {accuracy:.2f}%"
            )

        return self
