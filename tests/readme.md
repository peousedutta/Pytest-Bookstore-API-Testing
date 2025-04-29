## 🧪 Test Scenarios

### 🔐 Authentication

- ✅ Generate a valid JWT token using registered credentials
- ❌ Attempt to generate a token with invalid credentials
- ✅ Verify token-based access to protected endpoints

### 👤 User Management

- ✅ Register a new user with unique credentials
- ❌ Attempt to register a user with an existing username
- ✅ Validate user details via authorized call

### 📚 Book Management

- ✅ Fetch a list of all books available in the store
- ✅ Retrieve details of a specific book using a valid ISBN
- ❌ Attempt to retrieve a book using an invalid or missing ISBN

### 📥 User Book Collection

- ✅ Add a book to a user’s collection using valid token and ISBN
- ❌ Add a book with invalid token (unauthorized)
- ❌ Add a book with invalid or duplicate ISBN
- ✅ Remove a book from a user’s collection
- ✅ Delete all books from a user’s account
- ❌ Attempt delete with expired/missing token

### ⚠️ Error Handling & Negative Tests

- ❌ Access a secured endpoint without authentication
- ❌ Submit malformed JSON payloads
- ❌ Attempt operations on nonexistent user/book
- ❌ Use invalid HTTP methods (e.g., PUT on GET endpoint)
