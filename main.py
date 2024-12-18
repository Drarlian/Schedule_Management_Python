import sched
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo  # Python >= 3.9 (built in)
# import pytz  # Python < 3.9 (pip install pytz)

# Configuração do fuso horário
brazil_tz = ZoneInfo("America/Sao_Paulo")
# brazil_tz = pytz.timezone("America/Sao_Paulo")

scheduler = sched.scheduler(time.time, time.sleep)


def job1():
    print(f"Tarefa 1 executada: {datetime.now(tz=brazil_tz)}")

    # Reagendar para daqui a 4 dias às 10:00
    # next_run_on_function = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0) + timedelta(days=4)
    next_run_on_function = datetime.now(tz=brazil_tz) + timedelta(minutes=2)
    scheduler.enterabs(next_run_on_function.timestamp(), 1, job1)


def job2():
    print(f"Tarefa 2 executada: {datetime.now(tz=brazil_tz)}")

    # Reagendar para daqui a 4 dias às 10:00
    # next_run_on_function = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0) + timedelta(days=4)
    next_run_on_function = datetime.now(tz=brazil_tz) + timedelta(minutes=4)
    scheduler.enterabs(next_run_on_function.timestamp(), 1, job2)


# Primeira execução do Job 1:
# next_run = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
next_run_job1 = datetime.now(tz=brazil_tz).replace(hour=15, minute=20, second=0, microsecond=0)
if datetime.now(tz=brazil_tz) > next_run_job1:  # Se já passou das 10:00 de hoje, agende para daqui a 4 dias
    # next_run += timedelta(days=4)
    next_run_job1 += timedelta(minutes=2)
scheduler.enterabs(next_run_job1.timestamp(), 1, job1)


# Primeira execução do Job 2:
# next_run = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
next_run_job2 = datetime.now(tz=brazil_tz).replace(hour=15, minute=20, second=0, microsecond=0)
if datetime.now(tz=brazil_tz) > next_run_job2:  # Se já passou das 10:00 de hoje, agende para daqui a 4 dias
    # next_run += timedelta(days=4)
    next_run_job2 += timedelta(minutes=4)
scheduler.enterabs(next_run_job2.timestamp(), 1, job2)


print(f"Job 1 agendado para: {next_run_job1}")
print(f"Job 2 agendado para: {next_run_job2}")
scheduler.run()
