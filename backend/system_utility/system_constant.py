from typing import Dict

SERVICE_UNAVAILABLE_MESSAGE = 'Service temporarily unavailable, try again later.'
SERVICE_UNAVAILABLE_STRCODE = 'service_unavailable'
SYSTEM_UNKNOWN_ERR_MESSAGE = 'Some errors happen in the server. Please contact the system administrator.'
SYSTEM_UNKNOWN_ERR_STRCODE = 'unknown_error'


SYSTEM_CONSTANT: Dict = {SERVICE_UNAVAILABLE_STRCODE: SERVICE_UNAVAILABLE_MESSAGE,
                         SYSTEM_UNKNOWN_ERR_STRCODE: SYSTEM_UNKNOWN_ERR_MESSAGE

                         }

MONDAY = 'monday'
TUESDAY = 'tuesday'
WEDNESDAY = 'wednesday'
THURSDAY = 'thursday'
FRIDAY = 'friday'
SATURDAY = 'saturday'
SUNDAY = 'sunday'

SENIN = 'Senin'
SELASA = 'Selasa'
RABU = 'Rabu'
KAMIS = 'Kamis'
JUMAT = 'Jumat'
SABTU = 'Sabtu'
MINGGU = 'Minggu'

DAYS = [
  (SENIN, SENIN),
  (SELASA, SELASA),
  (RABU, RABU),
  (KAMIS, KAMIS),
  (JUMAT, JUMAT),
  (SABTU, SABTU),
  (MINGGU, MINGGU),
]
