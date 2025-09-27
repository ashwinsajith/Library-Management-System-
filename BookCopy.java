public class BookCopy {
    private final String copyId;
    private final Book book;
    private CopyStatus status;
    private String location=null;

    public BookCopy(Book book,String copyId, String location){
        this.book=book;
        this.copyId=copyId;
        this.status=CopyStatus.AVAILABLE;
        this.location=location;
    }

    public String getCopyId(){
        return this.copyId;
    }

    public CopyStatus getStatus(){
        return this.status;
    }

    public String getLocation(){
        return this.location;
    }

    public void markAsAvailable(){
        this.status=CopyStatus.AVAILABLE;
    }

    public void markAsCheckedOut(){
        this.status=CopyStatus.CHECKED_OUT;
    }

    public void markAsLost(){
        this.status=CopyStatus.LOST;
    }

    public boolean isAvailable(){
       return status==CopyStatus.AVAILABLE; //for enums == works best as only one instance of each constant exists.
    }

    public void setLocation(String location){
        this.location=location;
    }

    @Override
    public String toString(){
        return "Book: "+book.getTitle()+" | CopyID: "+ this.copyId+ " | ISBN: "+ book.getISBN()+ " | Status: "+ this.status+ " | Location: "+this.location;
    }

}
