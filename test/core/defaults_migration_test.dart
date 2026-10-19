import 'dart:convert';

import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:waqt/app/settings.dart';
import 'package:waqt/core/alerts.dart';
import 'package:waqt/core/prayer_calc.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test("old untouched defaults become the original app's, once", () async {
    // Saved by an older version: Iqama +15, Asr set by hand to +25.
    final old =
        const AlertConfig()
            .withPrayer(Prayer.dhuhr, const PrayerAlert(iqamaDelay: 15))
            .withPrayer(Prayer.asr, const PrayerAlert(iqamaDelay: 25))
            .withPrayer(Prayer.isha, const PrayerAlert(iqamaDelay: 15))
            .toJson()
          ..remove('jumuahFixed');
    SharedPreferences.setMockInitialValues({
      'alerts': jsonEncode(old),
      'imsak': 10,
    });
    final s = await AppSettings.load();
    expect(s.alerts.of(Prayer.dhuhr).iqamaDelay, 20);
    expect(s.alerts.of(Prayer.asr).iqamaDelay, 25, reason: 'set by hand');
    expect(s.alerts.of(Prayer.isha).iqamaDelay, 20);
    expect(s.alerts.jumuahFixedIqama, 13 * 60);
    expect(s.imsakMinutes, 15);

    // Done once: a later choice of 15 stays.
    await s.update(
      (x) => x.alerts = x.alerts.withPrayer(
        Prayer.dhuhr,
        const PrayerAlert(iqamaDelay: 15),
      ),
    );
    final again = await AppSettings.load();
    expect(again.alerts.of(Prayer.dhuhr).iqamaDelay, 15);
  });
}
