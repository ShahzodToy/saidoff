from googletrans import Translator
import polib

# Initialize translator
translator = Translator()

# Load the .po file
po_file = polib.pofile('locale/uz/LC_MESSAGES/django.po')

# Translate each entry
for entry in po_file:
    if not entry.translated():
        translated_text = translator.translate(entry.msgid, dest='uz').text
        entry.msgstr = translated_text

# Save the updated .po file
po_file.save()

# Compile the messages
import os
os.system('django-admin compilemessages')