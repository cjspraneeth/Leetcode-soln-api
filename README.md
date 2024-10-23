
# Leetcode-soln-api

**Leetcode-soln-api** is an API designed for fetching the expected time and space complexity for a Leetcode problem. The API provides several endpoints to retrieve information about problems by their number or their name from the problem's URL.

---

## **Table of Contents**
- [Endpoints](#endpoints)
  - [GET - List All Problems](#get---list-all-problems)
  - [GET - View Problem by Number](#get---view-problem-by-number)
  - [GET - View Problem by Link Name](#get---view-problem-by-link-name)
- [Usage](#usage)
- [Example Requests and Responses](#example-requests-and-responses)
  - [GET - List All Problems](#get---list-all-problems-1)
  - [GET - View Problem by Number](#get---view-problem-by-number-1)
  - [GET - View Problem by Link Name](#get---view-problem-by-link-name-1)

---

## **Endpoints**

### **GET - List All Problems**
- **URL:** `/api/problems`
- **Method:** `GET`
- **Description:** Retrieves a list of all problems available on Leetcode, along with their expected time and space complexities.

---

### **GET - View Problem by Number**
- **URL:** `/api/problems/by-number/:number`
- **Method:** `GET`
- **Description:** Retrieves details of a specific problem by its Leetcode problem number. The problem number should be provided in the URL path.

---

### **GET - View Problem by Link Name**
- **URL:** `/api/problems/by-name/:name`
- **Method:** `GET`
- **Description:** Retrieves details of a specific problem by its name (the name present in the Leetcode problem's URL).

---

## **Usage**

To use the API, make requests to the appropriate endpoint using the structure shown in the examples below. The API supports fetching a list of problems, retrieving a problem by its number, and retrieving a problem by its link name.

---

## **Example Requests and Responses**

### **GET - List All Problems**

- **Request:**
  ```
  GET http://127.0.0.1:8000/api/problems
  ```

- **Response:**
  ```json
  [
      {
          "id": 1,
          "problem_number": 1,
          "title": "Two Sum",
          "time_complexity": "O(n)",
          "space_complexity": "O(n)"
      },
      {
          "id": 2,
          "problem_number": 2,
          "title": "Add Two Numbers",
          "time_complexity": "O(n)",
          "space_complexity": "O(1)"
      }
  ]
  ```

- **Status Codes:**
  - `200 OK`: The request was successful and returned the list of problems.

---

### **GET - View Problem by Number**

- **Request:**
  ```
  GET http://127.0.0.1:8000/api/problems/by-number/1
  ```

- **Response:**
  ```json
  {
      "id": 1,
      "problem_number": 1,
      "title": "Two Sum",
      "time_complexity": "O(n)",
      "space_complexity": "O(n)"
  }
  ```

- **Status Codes:**
  - `200 OK`: The problem was found and returned.
  - `404 Not Found`: The requested problem number does not exist.

---

### **GET - View Problem by Link Name**

- **Request:**
  ```
  GET http://127.0.0.1:8000/api/problems/by-name/two-sum
  ```

- **Response:**
  ```json
  {
      "id": 1,
      "problem_number": 1,
      "title": "Two Sum",
      "time_complexity": "O(n)",
      "space_complexity": "O(n)"
  }
  ```

- **Status Codes:**
  - `200 OK`: The problem was found and returned.
  - `404 Not Found`: The requested problem name does not exist.

---

## **Contributing**
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## **License**
This project is licensed under the MIT License.
