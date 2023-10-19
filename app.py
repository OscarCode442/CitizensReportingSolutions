from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import requests

class CitizensReportingApp(App):
    def build(self):
        self.title = 'Citizens Reporting App'
        layout = BoxLayout(orientation='vertical')

        submit_button = Button(text='Submit Incident')
        submit_button.bind(on_press=self.submit_incident)
        view_button = Button(text='View Incidents')
        view_button.bind(on_press=self.view_incidents)

        layout.add_widget(submit_button)
        layout.add_widget(view_button)

        return layout

    def submit_incident(self, instance):
        # Implement incident submission logic
        # Gather data from the user (incident type, description, location, images)
        incident_type_input = TextInput(hint_text='Incident Type')
        description_input = TextInput(hint_text='Incident Description')
        latitude_input = TextInput(hint_text='Latitude')
        longitude_input = TextInput(hint_text='Longitude')

        submit_button = Button(text='Submit')
        submit_button.bind(on_press=self.send_incident_data)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(incident_type_input)
        layout.add_widget(description_input)
        layout.add_widget(latitude_input)
        layout.add_widget(longitude_input)
        layout.add_widget(submit_button)

        self.root_window.add_widget(layout)

    def send_incident_data(self, instance):
        # Gather incident data from input fields
        incident_type = instance.parent.children[0].text
        description = instance.parent.children[1].text
        latitude = instance.parent.children[2].text
        longitude = instance.parent.children[3].text

        # You can add image uploading logic here if needed

        # Create incident data dictionary
        incident_data = {
            'type': incident_type,
            'description': description,
            'latitude': latitude,
            'longitude': longitude,
            'images': ['image1.jpg', 'image2.jpg']  # Add image paths or URLs
        }

        # Send data to your WordPress server to create a new post
        # response = requests.post('https://your-wordpress-server.com/api/create-incident', json=incident_data)
        print(incident_data)

        # Handle the response (e.g., show success message or error message)

    def view_incidents(self, instance):
        # Implement incident viewing logic
        # Retrieve incident data from the server (WordPress) and display it in the app
        response = requests.get('https://your-wordpress-server.com/api/get-incidents')

        # Handle the response and display incident data in the app

if __name__ == '__main__':
    CitizensReportingApp().run()
