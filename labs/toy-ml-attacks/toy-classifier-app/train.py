from __future__ import annotations

from toy_classifier.model import MODEL_PATH, load_messages, predict_one, save_model, train_pipeline


def main() -> None:
    messages = load_messages()
    model = train_pipeline(messages)
    save_model(model, MODEL_PATH)

    validation_text = "urgent password reset verify account credential token"
    prediction = predict_one(model, validation_text)

    print(f"trained_messages={len(messages)}")
    print(f"saved_model={MODEL_PATH}")
    print(
        "validation_prediction="
        f"{prediction['label']} "
        f"phish_probability={prediction['phish_probability']:.3f}"
    )


if __name__ == "__main__":
    main()
