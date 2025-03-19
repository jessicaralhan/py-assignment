import pytest
import sqlite3
from unittest.mock import patch
from sqlite import schedule_appointment, update_appointments



def mock_connection_helper(query, params=()):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    if query.startswith("SELECT"):
        cursor.execute(query, params)
        return cursor.fetchall()
    else:
        cursor.execute(query, params)
        conn.commit()
    return None

class TestAppointments:
    @pytest.fixture  
    def db_connection(self):
        self.conn = sqlite3.connect(":memory:")
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE table appointments(
                    unique_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    date TEXT,
                    time TEXT,
                    description TEXT,
                    appointment_with TEXT
                )
    """)
        self.conn.commit()
        yield self.conn  
        self.conn.close()  

    def test_schedule_appointment(self, monkeypatch, db_connection):
        test_inputs = iter(["John Doe", "1", "2025-03-20", "10:30", "Checkup"])
        monkeypatch.setattr("builtins.input", lambda _: next(test_inputs)) 

        schedule_appointment(db_connection)

        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM appointments WHERE name = ?", ("John Doe",))
        result = cursor.fetchone()
        assert result is not None
        assert result[1] == "John Doe"
        assert result[2] == "2025-03-20"
        assert result[3] == "10:30"
        assert result[4] == "Checkup"
        assert result[5] == "Mr. Jug"

    def test_schedule_appointment_reprompt_time(self, monkeypatch, db_connection):
        test_inputs = iter(["John Doe", "1", "2025-03-20", "10:30", "Checkup"])
        monkeypatch.setattr("builtins.input", lambda _: next(test_inputs)) 

        schedule_appointment(db_connection)

        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM appointments WHERE name = ?", ("John Doe",))
        result = cursor.fetchone()
        assert result is not None
        assert result[1] == "John Doe"
        assert result[2] == "2025-03-20"
        assert result[3] == "10:30"
        assert result[4] == "Checkup"
        assert result[5] == "Mr. Jug"

        test_inputs = iter(["Mr. Alpha", "1", "2025-03-20", "10:30", "9:30", "Meet"])
        monkeypatch.setattr("builtins.input", lambda _: next(test_inputs)) 

        schedule_appointment(db_connection)

        cursor.execute("SELECT * FROM appointments WHERE name = ?", ("Mr. Alpha",))
        result = cursor.fetchone()
        
        assert result is not None
        assert result[1] == "Mr. Alpha"
        assert result[2] == "2025-03-20"
        assert result[3] == "9:30"
        assert result[4] == "Meet"
        assert result[5] == "Mr. Jug"
    
    def test_schedule_appointment_old_date_validation(self, monkeypatch, db_connection):
        test_inputs = iter(["Mr. King", "2", "2024-03-11", "10:30"])
        monkeypatch.setattr("builtins.input", lambda _: next(test_inputs)) 

        schedule_appointment(db_connection)

        cursor = db_connection.cursor()

        cursor.execute("SELECT * FROM appointments WHERE name = ?", ("Mr. King",))
        result = cursor.fetchone()

        assert result is None

    def test_schedule_appointment_wrong_date_format(self, monkeypatch, db_connection):
        test_inputs = iter(["Mr. King", "2", "20235354", "10:30"])
        monkeypatch.setattr("builtins.input", lambda _: next(test_inputs)) 

        schedule_appointment(db_connection)

        cursor = db_connection.cursor()

        cursor.execute("SELECT * FROM appointments WHERE name = ?", ("Mr. King",))
        result = cursor.fetchone()

        assert result is None

    def test_schedule_appointment_wrong_time_format(self, monkeypatch, db_connection):
        test_inputs = iter(["Mr. King", "2", "2025-12-12", "1014234"])
        monkeypatch.setattr("builtins.input", lambda _: next(test_inputs)) 

        schedule_appointment(db_connection)

        cursor = db_connection.cursor()

        cursor.execute("SELECT * FROM appointments WHERE name = ?", ("Mr. King",))
        result = cursor.fetchone()

        assert result is None

    def test_update_appointment(self, monkeypatch, db_connection):
        test_inputs = iter(["Aay", "2", "2025-12-12", "14:30", "Work"])
        monkeypatch.setattr("builtins.input", lambda _: next(test_inputs)) 

        schedule_appointment(db_connection)

        cursor = db_connection.cursor()

        cursor.execute("SELECT * FROM appointments WHERE name = ?", ("Aay",))
        result = cursor.fetchone()

        assert result is not None
        assert result[1] == "Aay"
        assert result[2] == "2025-12-12"
        assert result[3] == "14:30"
        assert result[4] == "Work"
        assert result[5] == "Mr. Young"

        test_inputs = iter(["1", "4", "2025-11-02", "12:30", "Meet"])
        monkeypatch.setattr("builtins.input", lambda _: next(test_inputs)) 

        update_appointments(db_connection)

        cursor.execute("SELECT * FROM appointments WHERE name = ?", ("Aay",))
        result = cursor.fetchone()
        
        assert result is not None
        assert result[1] == "Aay"
        assert result[2] == "2025-11-02"
        assert result[3] == "12:30"
        assert result[4] == "Meet"
        assert result[5] == "Mr Checo Perez"


    def test_update_appointment_not_exist(self, monkeypatch, db_connection):
        
        cursor = db_connection.cursor()

        test_inputs = iter(["3"])
        monkeypatch.setattr("builtins.input", lambda _: next(test_inputs)) 

        update_appointments(db_connection)

        cursor.execute("SELECT * FROM appointments WHERE unique_id = ?", ("3",))
        result = cursor.fetchone()
        
        assert result is None
        
    
