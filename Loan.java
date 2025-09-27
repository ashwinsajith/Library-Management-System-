import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

import static java.time.LocalDate.*;

public class Loan {
    private final String loanID;
    private BookCopy book;
    private Member member;
    private final LocalDate checkoutDate;
    private final LocalDate dueDate;
    private LocalDate returnDate;
    private LoanStatus status;
    private BigDecimal accruedFine;

    public Loan(String loanID,BookCopy book,Member member){
        this.loanID=loanID;
        this.book=book;
        this.member=member;
        this.checkoutDate=LocalDate.now();
        this.dueDate=checkoutDate.plusDays(15);
        this.returnDate=null;
        this.status=LoanStatus.ACTIVE;
        this.accruedFine=BigDecimal.ZERO;
    }

    public String getLoanID(){
        return this.loanID;
    }

    public String getBookCopy(){
        return book.toString();
    }

    public String getMember(){
        return member.toString();
    }

    public LocalDate getCheckoutDate() {

        return checkoutDate;
    }

    public LocalDate getDueDate() {
        return dueDate;
    }

    public LoanStatus getStatus() {
        return status;
    }

    public LocalDate getReturnDate() {
        return returnDate;
    }

    public BigDecimal getAccruedFine() {
        return accruedFine;
    }

    public void markAsActive(){
        this.status=LoanStatus.ACTIVE;
    }

    public boolean isActive(){
        return this.status.equals(LoanStatus.ACTIVE);
    }

    public boolean isOverdue(){
        return (this.isActive() && LocalDate.now().isAfter(dueDate));
    }

    public long daysLate(){
        if (returnDate==null) return 0;
        if (this.returnDate.isAfter(this.dueDate)){
            return this.dueDate.until(this.returnDate, ChronoUnit.DAYS);
        }
        return 0;
    }

    public void finalizeReturn(LocalDate actualReturn,BigDecimal dailyRate){
        this.returnDate=actualReturn;
        this.status=LoanStatus.RETURNED;
        BigDecimal days= BigDecimal.valueOf(this.daysLate());
        this.accruedFine= dailyRate.multiply(days).setScale(2, RoundingMode.HALF_UP);

    }


}
