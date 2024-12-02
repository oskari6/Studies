package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"
	"github.com/gorilla/mux"
	"github.com/gorilla/sessions"
	"github.com/google/uuid"
)

var store = sessions.NewCookieStore([]byte("secret-key"))
//USER
type User struct {
	ID string `json:"id"`
	Firstname string `json:"firstname"`
	Lastname string `json:"lastname"`
	Email string `json:"email"`
	Username string `json:"username"`
	Password string `json:"password"`
	RegisterDate time.Time `json:"register_date"`
	LastLogin time.Time `json:"last_login"`
}

var users = map[string]User{} // In-memory user store (username -> user object)

func main() {
	router := mux.NewRouter()
	//endpoints
	router.HandleFunc("/register", RegisterHandler).Methods("POST")
	router.HandleFunc("/login", LoginHandler).Methods("POST")
	router.HandleFunc("/logout", LogoutHandler).Methods("POST")

	fs := http.FileServer(http.Dir("./static"))
	router.PathPrefix("/").Handler(fs)

	http.Handle("/", enableCORS(router))
	//PORTS
	log.Println("Server starting on: 8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func RegisterHandler(w http.ResponseWriter, r *http.Request) {
	var newUser User
	err := json.NewDecoder(r.Body).Decode(&newUser)
	if err != nil || newUser.Username == "" || newUser.Password == "" {
		http.Error(w, "Invalid input", http.StatusBadRequest)
		return
	}

	if _, exists := users[newUser.Username]; exists {
		http.Error(w, "User already exists", http.StatusBadRequest)
		return
	}

	newUser.ID = uuid.New().String()
	newUser.RegisterDate = time.Now()

	users[newUser.Username] = newUser
	fmt.Fprintf(w, "User %s registered successfully!<br>Log in", newUser.Username)
}

func LoginHandler(w http.ResponseWriter, r *http.Request) {
	var loginUser User
	err := json.NewDecoder(r.Body).Decode(&loginUser)
	if err != nil || loginUser.Username == "" || loginUser.Password == "" {
		http.Error(w, "Invalid input", http.StatusBadRequest)
		return
	}

	storedUser, exists := users[loginUser.Username]
	if !exists || storedUser.Password != loginUser.Password {
		http.Error(w, "Invalid username or password", http.StatusUnauthorized)
		return
	}

	storedUser.LastLogin = time.Now()
	users[loginUser.Username] = storedUser
	
	fmt.Fprintf(w, "User %s logged in successfully!<br>Welcome to the site %s!", storedUser.Username, storedUser.Firstname)
}

func LogoutHandler(w http.ResponseWriter, r *http.Request){
	session, _ := store.Get(r, "session-name")
	session.Options.MaxAge = -1
	session.Save(r, w)

	fmt.Fprintf(w, "You have been logged out successfully!<br>Log in / Register")
}
//CORS varten koska backend portti on 8080 ja muuten tulee ongelmia
func enableCORS(next http.Handler)http.Handler {
  return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request){
	w.Header().Set("Access-Control-Allow-Origin", "*") // Allow all
        w.Header().Set("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE")
        w.Header().Set("Access-Control-Allow-Headers", "Content-Type")
		if r.Method == "OPTIONS"{
			w.WriteHeader(http.StatusOK)
			return
		}
		next.ServeHTTP(w, r)
  })
}