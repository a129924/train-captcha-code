def main():
    from torch import nn

    from .data_set import CaptchaDataSet
    from .loader import CaptchaLoader
    from .model import CNN
    from .train import CNNModelTrainer

    best_model_path = "./best_model/best_model_2.pth"

    dataset = CaptchaDataSet(config_path="./config/captcha_data_set.env")
    loader = CaptchaLoader(config_path="./config/train_config.env", dataset=dataset)

    train_loader, val_dataloader = loader.get_loaders()

    trainer = CNNModelTrainer(
        model=CNN(),
        dataset=dataset,
        train_loader=train_loader,
        test_loader=val_dataloader,
        criterion=nn.CrossEntropyLoss(),
        learning_rate=0.001,
    )

    (
        trainer.load_model_from_file(model_path=best_model_path)
        .train(model_save_path="./best_model/best_model_2.pth", num_epochs=10)
        .validate(num_epochs=10)
    )


if __name__ == "__main__":
    main()
