package adweb.userservice.controller.requests;

/**
 * @author yanhua
 */
public class AnswerRequest {
    private String qid;

    private String email;

    private String answer;

    public String getEmail() { return email;}

    public void setEmail(String email) { this.email = email;}

    public long getQid() { return qid;}

    public void setQid(String qid) { this.qid = qid;}

    public String getAnswer() { return answer;}

    public void setAnswer(String answer) { this.answer = answer;}
}
