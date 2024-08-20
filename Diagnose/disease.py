class Disease:
    """
    Creates object disease
    """

    def __init__(self, name, symptoms, description, urgent_care_needed, note):
        self.name = name
        self.symptoms = symptoms
        self.description = description
        self.urgent_care_needed = urgent_care_needed
        self.note = note

    # def __str__(self):
    #     return f"Disease: name={self.name}, symptoms={self.symptoms}, description={self.description}, urgent care needed={self.urgent_care_needed}, note={self.note}"

    def __str__(self):
        return f"{self.name}"
