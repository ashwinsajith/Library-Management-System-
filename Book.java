import java.util.Scanner;

public class Book {
    private final String isbn;
    private String title;
    private String author;
    private String publisher;
    private int year;
    private String subject;

    public Book(String isbn,String title, String author){
        this.isbn=normalizeISBN(isbn);
        this.title=title;
        this.author=author;
        this.year=0;
    }

    public String getISBN(){
        return this.isbn;
    }

    public String getTitle(){
        return this.title;
    }

    public String getAuthor(){
        return this.author;
    }

    public String getPublisher(){
        return this.publisher;
    }

    public int getYear(){
        return this.year;
    }

    public String getSubject(){
        return this.subject;
    }

    public void updateTitle(String newTitle){
        this.title=newTitle;
    }

    public void updateAuthor(String newAuthor){
        this.author=newAuthor;
    }

    public void updatePublisher(String newPublisher){
        this.publisher=newPublisher;
    }

    public void updateYear(int newYear){
        this.year=newYear;
    }

    public boolean matchesKeyword(String keyword){
        String key=keyword.trim().toLowerCase();
        return (title.toLowerCase().contains(key) || subject.toLowerCase().contains(key) || publisher.toLowerCase().contains(key) || author.toLowerCase().contains(key));
    }


    public static String normalizeISBN(String isbn){
        if (isbn==null) return "";
        String normalizedString=isbn.trim().replace("-","").replace(" ","").toUpperCase();
        return normalizedString;
    }

    @Override
    public String toString(){
        return "Book: "+this.title+"| ISBN: "+this.isbn+" Author: "+this.author;
    }

}
