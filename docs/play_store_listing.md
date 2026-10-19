# Play Store listing — Azan Time

## Package name (permanent)
com.azantime.namaz – store link: https://play.google.com/store/apps/details?id=com.azantime.namaz

## App name (max 30)
Azan Time: Namaz Prayer Times

## Short description (max 80)
Exact Azan & Namaz times, Qibla, Duas, Ramadan timetable – works offline

## Full description (max 4000)
Azan Time gives you exact prayer times for your place, a beautiful Azan at
every prayer, and everything a Muslim needs each day – fully offline, with no
ads and no tracking.

🕌 EXACT TIMES
• 507 yearly mosque calendars of Kerala, Karnataka, Tamil Nadu, the Gulf and
  more, used as printed when you are at that place
• Everywhere else, times calculated for your exact location with the method
  of your country (Karachi, Muslim World League, Umm Al-Qura, ISNA, Egyptian,
  Tehran, Ithna Ashari, or your own Custom Method)
• Shafi'i or Hanafi Asr, high-latitude rules, ± minute adjustments, or set
  your own fixed Azan time for any prayer
• Import your mosque's own timetable (CSV)

🔔 AZAN & IQAMA ALERTS
• Full recorded Azan, bell, chime, your phone's sound or your own MP3
• Separate Fajr sound, Iqama alerts and Iqama times per mosque
• Full-screen Azan over the lock screen, volume control, stop with a volume key
• Auto-silent the phone during prayers
• Always-on notification with the next Azan and a live countdown

✨ BEAUTIFUL & LIVELY
• Animated sky that follows the day – dawn, sun, sunset, moon and stars
• Live clock and countdown to the next prayer
• Home-screen widgets, including a tall poster widget with all five times

📤 SHARE THE TIMES
• Share today's or tomorrow's prayer times as a poster image – in 12
  languages – to WhatsApp and family groups

🧭 QIBLA
• Compass that glows and vibrates when you face the Kaaba, with the distance
  to Makkah

📿 DUAS, AZKAR & TASBIH
• Morning and evening adhkar, after-prayer adhkar and daily duas with Arabic,
  transliteration, meaning and a tap counter
• Tasbih counter for the after-prayer set

🌙 RAMADAN
• Suhoor and Iftar countdown, the full Ramadan timetable, Niyyah, Iftar and
  Laylat al-Qadr duas, Taraweeh and Suhoor alerts

📅 HIJRI CALENDAR
• Month calendar with Hijri dates and Islamic occasions (Ramadan, Eid,
  Arafah, Ashura, Mawlid and more), with a Hijri day correction

✅ PRAYER TRACKER
• Mark each prayer as prayed and keep your streak

🌍 12 LANGUAGES
English, മലയാളം, ಕನ್ನಡ, العربية, اردو, हिन्दी, தமிழ், বাংলা, Bahasa Indonesia,
Bahasa Melayu, Türkçe, Français

🔒 PRIVATE
No ads, no accounts, no tracking. Your location stays on your phone; the app
has no internet permission.

## Category
Lifestyle (or Books & Reference)

## Tags / keywords to use in the text
azan, adhan, namaz, salah, prayer times, qibla, ramadan, islamic calendar,
hijri, dua, tasbih, kerala, malayalam, kannada

## Screenshots (phone, 1080×1920, docs/store/screenshots/)
Upload all 7 in this order (made by tool/store_screenshots.py):
1_1_today, 2_12_share, 3_2b_calendar, 4_13_duas, 5_14_ramadan, 6_3_qibla,
7_5_alerts

## Data safety form
• Data collected: none
• Data shared: none
• Location: used on the device only, to calculate prayer times (not
  collected, not shared)

## Content rating
Everyone

## Store graphics (docs/store/)
• App icon 512×512: docs/store/icon-512.png
• Feature graphic 1024×500: docs/store/feature-graphic-1024x500.png

## Privacy policy URL
https://maheshraikg.github.io/azan-time/privacy.html
(Turn on GitHub Pages once: repository Settings → Pages → Source "Deploy from a
branch" → Branch `main`, folder `/docs` → Save.)

## Play Console declarations (App content)
• Foreground service – type "special use": keeps the next-prayer notification
  (time and countdown) always shown, which the user can turn off in Settings.
  Also "media playback": plays the Azan.
• Exact alarms (SCHEDULE_EXACT_ALARM): the Azan must sound at the exact prayer
  time; this is the app's core function (alarm/clock-like).
• Full-screen intent (USE_FULL_SCREEN_INTENT): shows the Azan over the lock
  screen at prayer time, like an alarm clock.
• Location: used on the device only for prayer times and Qibla.
• Ads: No. Target audience: everyone (not designed for children).

## Upload
1. Add the 4 upload-key secrets in GitHub (Settings → Secrets and variables →
   Actions): UPLOAD_KEYSTORE_BASE64, UPLOAD_KEYSTORE_PASSWORD,
   UPLOAD_KEY_ALIAS, UPLOAD_KEY_PASSWORD.
2. Push or run the "Build APK" workflow (Actions → Build APK → Run workflow).
3. Download azan-time.aab from the apk-latest release.
4. Play Console → Create app → Testing → Closed testing (12 testers, 14 days
   for new personal accounts) → upload azan-time.aab, with Play App Signing on.
5. After the test period: Production → upload the newest .aab.

## Before publishing
• Have a scholar check the Arabic of the duas and Ayat al-Kursi
  (lib/core/duas.dart)
• Sign the release with your own upload key
• Raise `version:` in pubspec.yaml for each upload
