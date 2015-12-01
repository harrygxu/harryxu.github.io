#!/usr/bin/osascript

on run argv
	
	set msgSubject to "Your SoCal PLS 2015 talk proposal"
	set msgFile to item 1 of argv
	
	set email to (do shell script ("basename " & (msgFile as text)))
	
	set filename to (do shell script "pwd") & "/" & (msgFile as text)
	set msgContents to (read POSIX file filename) as «class utf8»
	
	tell application "Mail"
		set msg to make new outgoing message with properties {subject:msgSubject, content:msgContents}
		
		tell msg to make new to recipient at end of every to recipient with properties {address:email}
	end tell
end run