package adweb.userservice.controller.requests;

public class LoginRequest {
    public String email;
    public String password;

    public LoginRequest(String username, String password) {
        this.email = username;
        this.password = password;
    }

    public LoginRequest() {
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
