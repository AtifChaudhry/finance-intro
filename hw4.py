#!/usr/bin/python

#### import the basic finace functions
import finance_formulas as fi

#### Collect answers in the ans array
ans = []

### Question 1
#### (5 points) The project with the highest IRR is always the project with the highest NPV.

False


### Question 2
#### (10 points) Ann Arbor is considering offering public bus service for free. 
#### Setting up the service will cost the city \$0.6M (where M stands for million). 
#### The useful life of the buses is 25 years. Annual maintenance of the buses 
#### would cost \$50,000 per year and they would need a major overhaul in year 15 
#### that will cost a total of \$350,000. This overhaul is in addition to the 
#### annual maintenance. Annual operating costs will begin at \$90,000 in year 1 
#### and grow at 2% per year thereafter. By using the buses as advertisement 
#### space, the city will generate a revenue of \$75,000 in year 1 and it will 
#### grow at 4% per year thereafter. Reduced parking requirements and other 
#### benefits generated by the project will save the city \$100,000/year. 
#### The salvage value (price city can get in the future after maintenance) 
#### of the used buses in year 25 is expected to be \$150,000. What is the NPV 
#### of the bus proposal? Ann Arbor does not pay taxes and the discount rate 
#### is 5%.

r        =  0.05        # 5%/yr discount rate
capex    = -0.6e6       # $0.6M setup cost
life     = 25           # usful life 25 years

main_yr  = -50e3        # $50,000/yr maintenance cost
main     = [main_yr] * life

opex_yr  = -90e3        # $90,000/yr operations expenses
opex_gr  = 0.02         # 2%/yr operations expense growth rate
opex     = [fi.comp(opex_yr, n, opex_gr) for n in range(0, life)]

advt_yr  = 75e3         # $75,000/yr advertisement revenue
advt_gr  = 0.04         # 4%/yr advertisement revenue growth rate
advt     = [fi.comp(advt_yr, n, advt_gr) for n in range(0, life)]

bene_yr  = 100e3       # $100,000/yr parking and other benefits
bene     = [bene_yr] * life

# Setup the cashflows by combining capex, expenses, revenues, & residual
cf       = [capex] + ([0] * life) 
for i in range(life):
    cf[i+1] = main[i] + opex[i] + advt[i] + bene[i]
cf[15]   += -350e3       # $350,000 one-time major overhaul in yr. 15 
cf[life] += 150e3        # $150,000 terminal value at end of life

npv = fi.npv(cf, r)

fi.rnd(npv)

### Question 3
#### (5 points) Your manager has the following two projects that he is considering, 
#### and wants to choose between them. Project A has an investment outlay/expense 
#### today of \$10,000, and its cash flows over the next three years are \$6,000, 
#### \$6,000, \$7,000. Project B has an outlay of \$20,000, and cash flows of \$10,000, 
#### \$12,000, and \$14,000. Which project should you advise your manager to choose?

'Cannot decide based on information'

### Question 4
#### (10 points) GE has the following two projects that it is considering; it can 
#### choose only one. Project A has an investment outlay/expense today of \$10M, 
#### and its cash flows over the next three years are \$4M, \$4M, \$5M. Project B 
#### has an outlay of \$10M, and cash flows of 0, 0, and \$14M. Which project 
#### should GE choose if the cost of capital for similar projects is 5%?

# Should not choose either.
# Project A
# Project B
# Do not have enough information

r    =  0.05 # 5%/yr discount rate
cf_a = [
#          CF  # Year
        -10e6, # 0 
          4e6, # 1
          4e6, # 2
          5e6  # 3
       ] 
cf_b = [
#          CF  # Year
        -10e6, # 0 
            0, # 1
            0, # 2
         14e6  # 3
       ] 
npv_a = fi.npv(cf_a, r)
npv_b = fi.npv(cf_b, r)

if (npv_a > npv_b):
    ans = 'Project A'
else:
    ans = 'Project B'

ans

### Question 5
#### (5 points) To get from net operating profits after tax (NOPAT) to free cash 
#### flows (FCF), you need to ADD back depreciation, SUBTRACT capital expenditures 
#### and ADD net working capital (i.e., current operating assets - current operating 
#### liabilities). (Free cash flow is another name for cash flows.)

# False.
# True.

False

### Question 6
#### (5 points) Last year your firm had revenue of \$20 million, cost of goods sold 
#### (COGS) of \$12 million, Selling, General, & Administration costs (SG&A) of \$2 
#### million, Account Receivables (AR) of \$6 million, Account Payables (AP) of \$4 
#### million and Inventory of \$4 million. What will be the free cash flow next/this 
#### year if you boost revenue 6% and AR 12%, while holding COGS growth to 3% and 
#### everything else remains the same as last year? (Assume no taxes and no new 
#### capital expenditures.) (You are encouraged to use a spreadsheet even for this 
#### specific type of question.)

rev     =  20e6 # Revenues
cogs    =  12e6 # COGS
sga     =   2e6 # SG&A

# Working Capital (WC)
ar      =   6e6 # AR
inv     =   4e6 # Inventory
ap      =   4e6 # AP

stmt = [
      + rev  * (1+0.06), # Revenues: up by 6%
      - cogs * (1+0.03), # COGS: up by 3%
      - sga,             # SG&A: unchanged
      - ar   * 0.12      # WC Change: 12% increase in AR
]

fcf = 0
for i in stmt: fcf += i

fi.rnd(fcf)

### Question 7
#### (15 points) Silver Bear Golf (SBG) is a manufacturer of top quality golf clubs 
#### with a specialty of putters. Currently, each putter they sell brings in \$200 
#### of revenue at a cost of \$150. This past year, they sold 1,000 putters and they 
#### expect this number to grow each year by 12% until this model becomes obselete 
#### after 10 more years. The foreman at the SBG factory recently brought to your 
#### attention a new technology that could lower the cost of production. This 
#### technology requires an upfront fixed investment of \$100,000 and has the capacity 
#### to produce all the putters you want to sell per year at a unit cost of \$135. 
#### There is no increased working capital need due to this new technology, and no 
#### value of the machine/technology after 10 years. What is the NPV of investing in 
#### the new technology? Ignore taxes and assume a discount rate of 9%. (Hint: Think 
#### incrementally; the difference between the world without and with this new 
#### technology! Also, ignoring taxes will be a big help if you think right.) 

r      = 0.09       # 9%/yr discount rate
life   = 10         # project lifetime
qty_yr = 1000       # the qty sold last year
qty_gr = 0.12       # 12%/yr
qty    = [fi.comp(qty_yr, i+1, qty_gr) for i in range(life)]

sales_price = 200   # $200/putter
cost_old    = 150   # $150/putter
profit_old  = sales_price - cost_old
rev_old     = [q * profit_old for q in qty]
cost_new    = 135
profit_new  = sales_price - cost_new
rev_new     = [q * profit_new for q in qty]
investment  = 100e3 # New tech. cost

# Cashflows: Investment and the delta of new and old revenues
cf = [-investment] + ([0] * life)
for i in range(life): cf[i+1] = rev_new[i] - rev_old[i]
npv = fi.npv(cf, r)

fi.rnd(npv)

### Question 8
#### (15 points) Fresh off the excitement of the 2012 London Olympic Games, you decide 
#### that you want your firm to take advantage of the profits to be made for the 2016 
#### games in Rio de Jeneiro. To do so you plan to open a factory in Brazil. After 
#### examining the idea, your CFO projects revenues next year (2013) to be \$15 million 
#### and costs to be \$9 million. Both of these are expected to grow at a rate of 25% 
#### per year as the excitement for the games builds. Your firm faces a 35% tax rate, 
#### a 14% discount rate and you can depreciate your new investment using the straight 
#### line method over the four years leading up to the games, at which point the value 
#### of the venture moving forward will be \$5 million. (This \$5 million is the terminal 
#### value that is in year 4 (that is, 2016) dollars and is the PV of all cash flows 
#### year 5 and beyond.) The capital expenditure of this project is \$12M. What is the 
#### NPV of the project? Assume that you have no significant working capital costs.
#### (Enter just the number without the \$ sign or a comma; round off decimals.) (You 
#### are strongly encouraged to use a spreadsheet.)

'<Missing!>'

### Question 9
#### (15 points) Walmart is considering opening a small experimental store in New 
#### York city. A store is expected to have a long economic life, but the valuation 
#### horizon is 10 years. The store in New York is likely to generate revenues of 
#### \$33M in the first year and then it grows at 5%. but the costs of running the 
#### business is high because the margins on all the products sold are low (it is 
#### a volume business!) The cost of goods sold are \$12M in year 1 and they are 
#### expected to grow at 4% per year thereafter. Selling and administration costs 
#### are likely to be \$1M every year as it is a small store. The tax rate is 35%. 
#### Walmart is so good at managing its stores that working capital increases can 
#### be assumed to be negligible. But since New York city is an expensive place, 
#### Walmart will have to invest \$200 million in purchasing a building (with land) 
#### even though it is a much smaller property than a usual Walmart store. The good 
#### news is that this outlay can be straight line depreciated over 10 years. Also, 
#### Walmart has estimated that the terminal value in year 10 dollars is \$100 million. 
#### This value is the value of all cash flows in year 11 and beyond. What is the NPV 
#### of opening this new store if the appropriate discount rate is 5%?(Again, all 
#### cash flows except initial investments happen at the end of the year. Enter 
#### just the number without the \$ sign or a comma; round off decimals.)
#### (You are strongly encouraged to use a spreadsheet.)

'<Missing!>'

### Question 10
#### (15 points) Springfield Ironworks (SI) recently had their furnace break down and 
#### they need to quickly purchase a new one to minimize the disruption in their 
#### production. They can either choose a high quality furnace (H) that costs 
#### \$110,000 with \$4,000 of annual maintenance costs for the 7-year life of the 
#### furnace, or a low quality furnace (L) that costs \$60,000 with \$7,500 in annual 
#### maintenance costs for the 4-year life of the furnace. Which furnace should SI 
#### choose? What is the annualized cost of their choice? Assume a discount rate of 
#### 6%, and ignore all taxes.

r = 0.06        # 6%/yr discount rate

# H: High Quality Furnace
price_h    = 110e3                          # $110,000 purchase price
maint_h    = 4e3                            # $4,000/yr maintenance
life_h     = 7                              # 7 years lifetime
cf_h       = [price_h] + [maint_h] * life_h # cashflow for life of furnace
npv_h      = fi.npv(cf_h, r)                # npv of cashflow at 6% 
ann_cost_h = fi.pmt(npv_h, life_h, r)       # annulaized cost computed as payments

# L: Low Quality Furnace
price_l    = 60e3                           # $60,000 purchase price
maint_l    = 7.5e3                          # $7,500/yr maintenance
life_l     = 4                              # 4 years lifetime
cf_l       = [price_l] + [maint_l] * life_l # cashflow for life of furnace
npv_l      = fi.npv(cf_l, r)                # npv of cashflow at 6% 
ann_cost_l = fi.pmt(npv_l, life_l, r)       # annulaized cost computed as payments

if (ann_cost_l < ann_cost_h):
    ans = '(L, %d)' % fi.rnd(ann_cost_l)
else:
    ans = '(H, %d)' % fi.rnd(ann_cost_h)

ans

# Print answers from the ans array
fi.print_lines(ans)
