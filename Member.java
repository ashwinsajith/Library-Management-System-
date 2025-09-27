import java.time.LocalDate;

public class Member {
    private final String memberId;
    private String fullName;
    private String email;
    private String phone;
    private boolean active;
    private final LocalDate joinedOn;
    private String notes;


    public Member(String memberId,String fullName){
        this.memberId=memberId;
        this.fullName=fullName;
        this.joinedOn=LocalDate.now();
        this.active=true;
        this.notes="";
    }

    public String getMemberId(){
        return this.memberId;
    }

    public String getFullName(){
        return this.fullName;
    }

    public String getEmail(){
        return this.email;
    }

    public String getPhone(){
        return this.phone;
    }

    public boolean isActive(){
        return this.active;
    }

    public LocalDate getJoinDate(){
        return this.joinedOn;
    }

    public String getNotes(){
        return this.notes;
    }

    public void updateName(String newName){
        this.fullName=newName;
    }

    public void updatePhone(String newPhone){
        if (newPhone != null){
            this.phone=newPhone.trim();
        }
    }

    public void updateEmail(String newEmail){
        if (newEmail != null){
            this.email=newEmail.trim();
        }
    }

    public void activate(){
        this.active=true;
    }

    public void suspend(){
        this.active=false;
    }


    public String contactInfo(){
        if (this.email == null && this.phone==null){
            return "No Contact info provided.";
        }else if (this.email==null) return "Phone: "+this.phone;
        else if (this.phone==null) return "Email: "+this.email;

        return "Email: "+this.email+" | Phone: "+this.phone;
    }

    @Override
    public String toString(){
        return "MemberID: "+this.memberId+" | Name: "+this.fullName+ " | Joined On: "+this.joinedOn+ " | Active: "+this.active;
    }
    
}
