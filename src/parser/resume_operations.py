class ResumeAnalyzer:
    def __init__(self, text: str):
        self.text = text

    def get_headings(self)->list:
        """ 
        Extracts headings from a PDF file.

        Args:
            text (str): Text from the PDF file.

        Returns:
            list: List of headings from the PDF file.
        """

        lines = self.text.split("\n")
        
        allowedHeadings = ['Experience Highlights', 'Areas of Leadership', 'Career Summary', 'Experience', 'Summary', 'Employment History', 'Professional Background', 'Professional History', 'Areas of Experience', 'Areas of Specialization', 'Technical Skills', 'Career', 'Certifications', 'Work Experience', 'Areas of Expertise', 'Areas of Strength', 'Areas of Knowledge', 'Career Experience', 'Languages', 'Profile', 'Publications', 'Skills Summary', 'Areas of Interest', 'References', 'Research', 'Professional Experience', 'Achievements', 'Experience Profile', 'Areas of Responsibility', 'Areas of Concentration', 'Projects', 'Skills', 'Career Highlights', 'Areas of Competence', 'Professional Profile', 'Core Competencies', 'Areas of Focus', 'Experience Summary', 'Employment', 'Objective', 'Core Strengths', 'Interests', 'Work History', 'Courses', 'Professional Summary', 'Strengths', 'Professional Skills', 'Education', 'Career Profile', 'Internship Experience']
        
        headings = []

        for line in lines:
            if line.strip() != "":
                if line in allowedHeadings:
                    headings.append(line)
        if len(headings) == 0:
            headings.append("Summary")
        return headings
    
    def get_formatted_output(self) -> dict:
        """ 
        Formats the resume data into a dictionary of headings and their corresponding data.

        Args:
            text (str): Text from the PDF file.

        Returns:
            dict: Dictionary containing the formatted output.
        """

        data: dict[str, list[str]] = {x: [] for x in ResumeAnalyzer(self.text).get_headings()}

        if len(data) > 1:
            lines = self.text.split("\n")
            current_heading = ""

            for line in lines:
                if line.strip() in data:
                    current_heading = line.strip()
                elif current_heading:
                    data[current_heading].append(line.strip())
        else:
            data["Summary"].append(self.text)

        return data