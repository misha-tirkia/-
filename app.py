from ext import app
from routes import logout, about, profile, contact, home, delete_news as delete, mains as cardinfo, login, signup

app.run(debug=True, host='0.0.0.0')   