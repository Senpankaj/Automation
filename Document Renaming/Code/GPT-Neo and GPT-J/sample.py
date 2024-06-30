from transformers import GPTNeoForCausalLM, GPT2Tokenizer

def main():
    # Load the model and tokenizer
    model_name = "EleutherAI/gpt-neo-125M"  # Smaller model for testing
    model = GPTNeoForCausalLM.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Define the prompt
    prompt = "What is the day today?"

    # Tokenize the input
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate the response
    outputs = model.generate(inputs.input_ids, max_new_tokens=50, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print("Generated Text:")
    print(generated_text)

if __name__ == "__main__":
    main()
