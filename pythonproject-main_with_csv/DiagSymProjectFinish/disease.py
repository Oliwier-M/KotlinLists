class Disease:

    def __init__(self, name, symptoms, description, urgent_care_needed, note):
        """Disease object created to store, name, symptoms, description, 
        if urgent care is needed and an additional note.

        Args:
        name(string): name of the disease 
        symptoms(list): list of symptoms associated with the disease
        description(string): description of the disease 
        urgent_care_needed(boolean): a boolean expression, if urgent help is needed = True, if not = False
        note(string): a note regarding the disease 
        """
        self.name = name
        self.symptoms = symptoms
        self.description = description
        self.urgent_care_needed = urgent_care_needed
        self.note = note

    # def __str__(self):
    #     return f"Disease: name={self.name}, symptoms={self.symptoms}, description={self.description}, urgent care needed={self.urgent_care_needed}, note={self.note}"

    def __str__(self):
        return f"{self.name}"


