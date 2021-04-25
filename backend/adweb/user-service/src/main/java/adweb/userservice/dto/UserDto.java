package adweb.userservice.dto;

public class UserDto {
    private String email;
    private String fullName;

    public UserDto(String email, String fullName) {
        this.email = email;
        this.fullName = fullName;
    }

    public UserDto() {
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getFullName() {
        return fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }
}
