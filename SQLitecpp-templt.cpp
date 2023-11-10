#include <SQLiteCpp/SQLiteCpp.h>
#include <iostream>

int main() {
    try {
        // Open a database file
        SQLite::Database db("example.db3", SQLite::OPEN_CREATE | SQLite::OPEN_READWRITE);

        // Create a table
        db.exec("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)");

        // Insert some data
        db.exec("INSERT INTO users (name, age) VALUES ('John Doe', 30)");
        db.exec("INSERT INTO users (name, age) VALUES ('Jane Doe', 25)");

        // Query the data
        SQLite::Statement query(db, "SELECT * FROM users");

        while (query.executeStep()) {
            // Get the results
            int id = query.getColumn(0);
            std::string name = query.getColumn(1);
            int age = query.getColumn(2);

            // Print the results
            std::cout << "ID: " << id << ", Name: " << name << ", Age: " << age << std::endl;
        }
    } catch (std::exception& e) {
        std::cerr << "SQLite exception: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}