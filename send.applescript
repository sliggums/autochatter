on run {contactName, targetMessage}
	tell application "Messages"
		set targetBuddy to first participant whose name is contactName
		send targetMessage to targetBuddy
	end tell
end run
