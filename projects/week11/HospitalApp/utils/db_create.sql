CREATE TABLE IF NOT EXISTS User(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username varchar(32) NOT NULL,
    hashed_password varchar(32) NOT NULL,
    user_type varchar(8) check (user_type in ('doctor', 'patient')),
    UNIQUE(id, username)
);

CREATE TABLE IF NOT EXISTS Patient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL, 
    full_name VARCHAR(32) NOT NULL,
    age INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES User(id)
);

CREATE TABLE IF NOT EXISTS Doctor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    full_name VARCHAR(32) NOT NULL,
    specialty VARCHAR(32) NOT NULL,
    phone VARCHAR(13) NOT NULL,
    FOREIGN KEY(user_id) REFERENCES User(id)
);

CREATE TABLE IF NOT EXISTS Slots(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER NOT NULL,
    start_hour VARCHAR(5) CHECK (start_hour LIKE '__:__'),
    end_hour VARCHAR(5) CHECK (start_hour LIKE '__:__'),
    reserved_date NOT NULL,
    reserved_status BIT DEFAULT 0 NOT NULL,
    FOREIGN KEY(doctor_id) REFERENCES Doctor(id)
);

CREATE TABLE IF NOT EXISTS Reservations(
    patient_id INTEGER NOT NULL,
    slot_id INTEGER NOT NULL,
    done_status varchar(8) check (done_status in ('ready', 'pending', 'canceled')),
    FOREIGN KEY(patient_id) REFERENCES Patient(id),
    FOREIGN KEY(slot_id) REFERENCES Slots(id)
);