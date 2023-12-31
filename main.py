import mysql.connector
from datetime import datetime


def display_menu():
    print("\nMenu:")
    print("1. Insert a new note")
    print("2. Update a note")
    print("3. Delete a note")
    print("4. Exit")


try:
    mydb = mysql.connector.connect(
        host="-",
        port="-",
        user="admin",
        password="-",
        database="-"
    )

    if mydb.is_connected():
        print("Connected to the database!")

        while True:
            display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                title = input("Enter note title: ")
                content = input("Enter note content: ")
                tags = input("Enter comma-separated tags: ")
                category = input("Enter note category: ")

                insert_query = """
                INSERT INTO main_table.notes (title, content, creation_date, tags, category, modified_date)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                note_data = (title, content, datetime.now(), tags, category, datetime.now())
                mycursor = mydb.cursor()
                mycursor.execute(insert_query, note_data)
                mydb.commit()
                print("New note inserted successfully")

            elif choice == '2':
                update_title = input("Enter the title of the note to update: ")
                new_content = input("Enter updated content: ")
                update_query = "UPDATE main_table.notes SET content = %s WHERE title = %s"
                mycursor = mydb.cursor()
                mycursor.execute(update_query, (new_content, update_title))
                mydb.commit()
                print("Note updated successfully")

            elif choice == '3':
                delete_title = input("Enter the title of the note to delete: ")
                delete_query = "DELETE FROM main_table.notes WHERE title = %s"
                mycursor = mydb.cursor()
                mycursor.execute(delete_query, (delete_title,))
                mydb.commit()
                print("Note deleted successfully")

            elif choice == '4':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

        mydb.close()
    else:
        print("Failed to connect to the database.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
