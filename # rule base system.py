

class ExpertSystem:

    def __init__(self):
        self.facts = set()
        self.rules = []
        self.inference_log = []

    def add_rule(self, conditions, conclusion):
        self.rules.append((conditions, conclusion))

    def add_fact(self, fact):
        self.facts.add(fact)

    def forward_chaining(self):

        new_fact_added = True

        while new_fact_added:
            new_fact_added = False

            for conditions, conclusion in self.rules:

                if all(condition in self.facts for condition in conditions):

                    if conclusion not in self.facts:

                        self.facts.add(conclusion)

                        self.inference_log.append(
                            f"Rule Applied: {conditions} ---> {conclusion}"
                        )

                        new_fact_added = True

    def display_results(self):

        print("\n" + "=" * 50)
        print("INFERENCE LOG")
        print("=" * 50)

        if self.inference_log:
            for step in self.inference_log:
                print(step)
        else:
            print("No rule was triggered.")

        print("\n" + "=" * 50)
        print("FINAL FACTS / CONCLUSIONS")
        print("=" * 50)

        for fact in sorted(self.facts):
            print("•", fact)


expert = ExpertSystem()

expert.add_rule(["fever", "cough"], "flu")

expert.add_rule(
    ["flu", "body_pain"],
    "viral_infection"
)

expert.add_rule(
    ["sneezing", "runny_nose"],
    "cold"
)

expert.add_rule(
    ["cold", "mild_fever"],
    "seasonal_cold"
)

expert.add_rule(
    ["viral_infection", "weakness"],
    "consult_doctor"
)

# User Input

print("=" * 50)
print("RULE-BASED EXPERT SYSTEM")
print("=" * 50)

print("\nAvailable Symptoms:")
print("fever")
print("cough")
print("body_pain")
print("sneezing")
print("runny_nose")
print("mild_fever")
print("weakness")

user_input = input(
    "\nEnter symptoms separated by comma: "
)

symptoms = user_input.lower().split(",")

for symptom in symptoms:
    expert.add_fact(symptom.strip())

# Run Inference Engine

expert.forward_chaining()

# Show Results

expert.display_results()