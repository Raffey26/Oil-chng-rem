from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ReminderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.input = TextInput(multiline=False, input_filter='int', hint_text='Enter 5 digits')
        self.input.bind(on_text_validate=self.set_reminder)
        layout.add_widget(self.input)

        button_layout = BoxLayout(orientation='horizontal')

        enter_button = Button(text='Enter Reminder')
        enter_button.bind(on_press=self.set_reminder)
        button_layout.add_widget(enter_button)

        change_button = Button(text='Change Reminder')
        change_button.bind(on_press=self.change_reminder)
        button_layout.add_widget(change_button)

        layout.add_widget(button_layout)

        self.reminder_label = Label(text='')
        layout.add_widget(self.reminder_label)

        self.reminder_set = False

        # Add a TextInput for entering current readings
        self.readings_input = TextInput(multiline=False, input_filter='int', hint_text='Enter current readings')
        layout.add_widget(self.readings_input)

        # Add a button to enter current readings and check reminder
        enter_reading_button = Button(text='Enter Current Readings')
        enter_reading_button.bind(on_press=self.enter_current_readings)
        layout.add_widget(enter_reading_button)

        return layout

    def set_reminder(self, instance):
        input_text = self.input.text

        if len(input_text) != 5:
            self.reminder_label.text = 'Please enter 5 digits.'
            return

        self.reminder_set = True
        self.reminder = int(input_text)
        self.reminder_label.text = f'Reminder is set for {self.reminder}'

    def change_reminder(self, instance):
        self.reminder_set = False
        self.reminder_label.text = 'Reminder cleared. Please enter a new 5-digit reminder.'

    def enter_current_readings(self, instance):
        current_readings = self.readings_input.text
        self.readings_input.text = current_readings
        self.check_reminder(None)

    def check_reminder(self, instance):
        if not self.reminder_set:
            self.reminder_label.text = 'Please set a reminder first.'
            return

        input_text = self.readings_input.text

        if not input_text:
            self.reminder_label.text = 'Please enter a number to check.'
            return

        input_value = int(input_text)
        diff = abs(input_value - self.reminder)

        if input_value == self.reminder:
            self.reminder_label.text = 'Reminder: Do not forget to get oil changed!'
        elif input_value < self.reminder:
            self.reminder_label.text = f'You still have {diff} kms left before oil change.'
        else:
            self.reminder_label.text = 'Please get oil changed!'


if __name__ == '__main__':
    ReminderApp().run()
