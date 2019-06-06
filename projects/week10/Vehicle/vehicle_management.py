import sqlite3

def list_all_free_hours():
    connection = sqlite3.connect('vehicle.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT (id, date, start_hour) FROM RepairHour;
        """
    )

    connection.commit()
    connection.close()

if __name__ == "__main__":
    print("Hello User")
    list_all_free_hours()