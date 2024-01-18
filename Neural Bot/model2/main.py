from analyze import analyze_response
model = analyze_response("no-context")

while True:
    question=input(">> ")
    print(model.queue(question))