config = {
    "myopenkey": "YOUR_API_KEY",
    "modelname": "gpt-4o",
    "jsonbuild": """
            Analyse the following text return the results in a structured JSON format in english without a markdown viewer. The result must contain following components:

            "Transcript": The text should be fully reproduced.  
            "Eindruck": Reflect on the content and how well the text reflects the values of commoning. Assess which aspects of the text particularly align with the logic of commoning and which may potentially contradict it.
            "Gemeinschaft": Provide a rating between 0 and 100 that expresses how strongly the sense of connection among people is depicted in the text (0 = very selfish, 100 = very community-oriented).  
            "Vertrauen": Provide a rating between 0 and 100 that expresses how trustworthy the text appears (0 = very distrustful, 100 = very trustworthy).  
            "Gegenseitig": Provide a rating between 0 and 100 that expresses how inviting and open the text is for collaboration (0 = very dismissive, 100 = very inviting).  
            "Nachhaltig": Provide a rating between 0 and 100 that expresses how consciously the text manages resources (0 = very wasteful, 100 = very mindful and frugal).  
            "Inklusion": Provide a rating between 0 and 100 that expresses how inclusive the text is (0 = exclusive, 100 = inclusive).  
            "Kommerziell": Provide a rating between 0 and 100 that expresses how much the text reflects profit-oriented economic practices (0 = needs-oriented, 100 = profit-oriented).  
            "SozialesMiteinander": Provide a rating between 0 and 100 that expresses how much the text supports collaboration and the fostering of relationships (0 = antisocial, 100 = very social).  
            "GleichrangigeSelbstOrganisation": Provide a rating between 0 and 100 that expresses how much the text promotes negotiating on equal terms (0 = hierarchical, 100 = equal).  
            "SorgendesSelbstbestimmtesWirtschaften": Provide a rating between 0 and 100 that expresses how much the text supports caring and self-determined economic practices (0 = externally controlled, 100 = self-determined and needs-oriented). 
            
            The User Text is: 
            """
}
