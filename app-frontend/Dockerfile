# שלב 1: בחירת אימג' בסיס
# אנו משתמשים באימג' הרשמי של Nginx (שרת ווב קל משקל) בגרסת alpine.
FROM nginx:alpine

# שלב 2: העתקת קבצים
# אנו מעתיקים את קובץ ה-HTML שלנו לנתיב ברירת המחדל ש-Nginx מגיש ממנו קבצים.
COPY index.html /usr/share/nginx/html/index.html

# שלב 3: חשיפת פורט
# שרת Nginx מאזין כברירת מחדל על פורט 80.
EXPOSE 80
