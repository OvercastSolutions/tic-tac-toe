Authors: Derek Williams and Stef Timmermans (Overcast Solutions)
Last Modified: September 8, 2021

Description:

Using Flask  on Windows:
	Ensure Flask is updated to version 21.2.4.

	Virtual Machine steps for Windows (cmd) in directory path:
		1) py -m venv
		2) end\Scripts\activate
		3) pip install flask
		4) set FLASK_APP = app.py
		5) flask run

	To quit:
		6) CTRL+C
		7) deactivate