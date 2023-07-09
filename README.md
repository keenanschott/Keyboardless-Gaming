# Keyboardless-Gaming

## Setup

A valid [Python](https://www.python.org/downloads/) installation, [SpeechRecognition](https://pypi.org/project/SpeechRecognition/), [Dotenv](https://pypi.org/project/python-dotenv/), and a few other miscellaneous libraries. A [wit.ai](https://wit.ai/) API key will also be needed; this can also be substituted for other speech recognition endpoints, see [here](https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py) for an example.

## Minecraft

The program assumes default key bindings, sneak to be on a toggle, and sprint to be a held key. The voice commands are as follows:

| Voice Command | Result |
|---------------|--------|
| Jump | The player will jump once. |
| Sneak | Sneak will be toggled on/off. |
| Sprint | The player will sprint. |
| Move | The player will move forward. |
| Back | The player will move backwards. |
| Left | The player will strafe to the left. |
| Right | The player will strafe to the right. |
| Drop | The player will drop the item currently selected on the hotbar. |
| Inventory | The inventory menu will open/close. |
| Swap | The player will swap items between hands. |
| Players | In multiplayer, the list of players will open. |
| Close | In multiplayerm, the list of players will close. |
| Stop | The player will stop all movement. |

## League of Legends

The program assumes default key bindings with the exception of the "R" ability, which I have binded to "T". The voice commands are as follows:

| Voice Command | Result |
|---------------|--------|
| One | The player will use the "Q" ability. |
| Two | The player will use the "W" ability. |
| Three | The player will use the "E" ability. |
| Four | The player will use the "R" ability. |
| Five | The player will use the summoner spell in the first slot. |
| Six | The player will use the summoner spell in the second slot. |
| Shop | The player will open/close the shop. |