from sqlalchemy import (Integer,
                        Numeric , 
                        CheckConstraint,)

from sqlalchemy.orm import Mapped , mapped_column ,DeclarativeBase
from decimal import Decimal


class Base(DeclarativeBase):
    pass


class EmployeePayDeatils(Base) :

    __tablename__ = "employee_salary"

    __table_args__ = ( 
       
        CheckConstraint("basic_salary>5000",
                        name="ck_basic_salary"),

        CheckConstraint("da>0",
                        name="ck_positive_da"),

        CheckConstraint("pf>0",
                        name="ck_positive_pf"),

        CheckConstraint("gross_salary>basic_salary",
                        name="ck_gross_higher_than_base")
                        
    )

    employee_id: Mapped[int] =  mapped_column( Integer , 
                                              primary_key= True )

    basic_salary: Mapped[Decimal] = mapped_column (Numeric(12,2),
                                                   nullable=False)

    da:Mapped[Decimal] = mapped_column (Numeric(12,2),
                                        nullable=False)

    pf:Mapped[Decimal]=mapped_column (Numeric(12,2),
                                    nullable=False)

    gross_salary:Mapped[Decimal]=mapped_column(Numeric(12,2),
                                               nullable=False)

    new_basic_salary: Mapped[Decimal] = mapped_column (Numeric(12,2),
                                                       nullable=False)

    

    

    
    