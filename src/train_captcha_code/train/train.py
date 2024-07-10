from torch import Tensor
from typing_extensions import Self, override

from .base import ModelBaseTrainer


class ModelTrainer(ModelBaseTrainer):
    def caculate_loss_value(self, outputs: Tensor, labels: Tensor) -> Tensor:
        """
        caculate_loss_value 計算train階段 predict label跟true label之間的相似度

        Args:
            outputs (Tensor): 多個train過model的值
            labels (Tensor): 多個true labels

        Returns:
            Tensor: 回傳相似度
        """
        from torch import zeros

        loss: Tensor = zeros(1, requires_grad=True)
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

            if epoch_loss > best_loss:
                from torch import save

                best_loss = epoch_loss
                save(self.model.state_dict(), model_save_path)

            self.logger.info(msg=f"第{epoch}次訓練結束")

        return self

    def process_train_batch(self) -> float:
        """
        process_train_batch 處理計算train階段每一次batch的loss值

        Returns:
            float: 當次batch的loss值
        """
        from torch.autograd import Variable

        running_loss: float = 0.0
        for batch in self.train_loader:
            images = Variable(batch.image)
            labels = Variable(batch.label_index)

            self.optimizer.zero_grad()  # 清除梯度
            outputs = self.model(images)  # 前向傳播
            # 計算損失
            loss = self.caculate_loss_value(outputs=outputs, labels=labels)

            loss.backward()  # 反向傳播
            self.optimizer.step()  # 更新權重

            running_loss += loss.item()

        return running_loss
