Program Description
Data Structures
The program leverages custom data structures to represent financial assets: Stock and Bond. These structures encapsulate various attributes related to these assets and provide methods to interact with and manipulate the data:

Stock:

Attributes: ticker (symbol representing the stock), price (current price), and company (name of the company).
Custom methods: A string representation method and sorting capabilities based on price.
Bond:

Attributes: price (current price), description (detailed description of the bond), duration (years to maturity), and yeildAmt (yield percentage).
Custom methods: A string representation method and sorting capabilities based on yield.
Both Stock and Bond extend a common base class Asset, which ensures that all asset types maintain a consistent interface and structure.

Object-Oriented Programming (OOP)
The program utilizes key OOP principles to design a flexible and reusable system:

Encapsulation: The attributes and methods related to Stock and Bond are bundled together within their respective classes. This encapsulation ensures that data manipulation is controlled and predictable.
Inheritance: The Stock and Bond classes inherit from an abstract base class Asset, promoting code reuse and reducing redundancy. The Sort class provides sorting functionality that can be utilized by both Stock and Bond classes.
Polymorphism: Through the use of abstract methods and overridden methods in the derived classes, the program supports polymorphism. This allows different asset types to be processed using a common interface while ensuring specific behavior for each asset type.
Abstraction: The Asset class defines the blueprint for all asset types, hiding the complex implementation details from the user and exposing only the necessary interface.
Advanced Algorithms
The program incorporates advanced algorithms to enhance functionality, particularly in sorting the financial assets:

Merge Sort:
The Sort class implements the merge sort algorithm, a classic divide-and-conquer sorting technique. Merge sort is efficient with a time complexity of O(n log n) and ensures stable sorting.
The algorithm splits the list of assets into halves, recursively sorts each half, and then merges the sorted halves back together. This approach guarantees a consistently efficient sort, even for large datasets.
Integration of Concepts
By combining these data structures, OOP principles, and advanced algorithms, the program provides a robust and efficient system for managing and sorting financial assets. It ensures that:

Users can create and interact with different types of assets in a uniform manner.
Sorting functionality is built-in and can handle complex objects based on specified criteria (price for stocks and yield for bonds).
The system is extendable, allowing for new asset types to be added with minimal changes to the existing codebase.
Conclusion
This program exemplifies how fundamental computer science concepts can be integrated to solve real-world problems effectively. By leveraging data structures, object-oriented programming, and advanced algorithms, it creates a powerful tool for financial asset management, demonstrating the synergy between these foundational elements.
