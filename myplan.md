My Plan

1. Study the take home exam

Expectations:
- Insightful analysis
- Elegant code
- Clear documentation of findings (?In different color?)
- Keep code/result even if not directly answering the question

Hints:
- Google solutions without complicated code
- Thoughts in pseudo code for extra ideas permissable

Additional ideas:
- Contribute to improving this task


Spirit of the task
- Validate and monitor 2 models that predict if customers will repay all scheduled payments in the coming X month

Part I
Task 1.1 Data Cleaning (A few surprises)
Routine checks:
- Dtypes: unique_id,date,status
- NAs? NaN?
- Unique Values?
- Duplicates (mb later)

1. monthly_outcome:
    - Payment status at each payment date
    - Type: String
    - Unique values: 0,1,2,3,4,D
        - D is terminal status, all following entries are D
    - Q:
        - How many events per customer? When is all payed back?
        - Missing entries? Duplicated entries? Gaps?
        - Monotonally increasing?
        - Is it always 12 payback dates?
        - What are the payment dates? 1st of month?

2. application:
 - unique_id,stress_score,is_bad_12m,model_1,model_2,origination_date,loan_term,loan_amount,age_oldest_account,total_value_of_mortgage,current_utilisation,months_since_2_payments_missed,number_of_credit_searches_last_3_months
 - available for every unique_id?

Task 1.2 Another target

Part II
- Split by loan application date? (originate date?) <2019-08-01, between 2019-08-01 AND 2020-01-01, > 2020-01-01
- Compare size of train, test, post deployment
- Could we have randomised over unique users?

Compare the 2 models, used for 
- Loan approval: Threshold for at least 3 missing in 12 months?
- Loss estimate: Default probability
- Pricing: Interest rate to be charged


Task 2.1
- Calculate ROC curve and calculate AUC for both models
- Prediction power is all we care, why also not take the other model... no idea right now what he means

Task 2.2
- Create segments
- Compare model scores within them

Task 2.3
- Predict rate of bad vs actual bad rate?

Task 2.4 No idea whats going on there

Part III
Task 3.1
Compare recall precision accuracy to test set?
Confusion matrix? More?

3.2
Segments?

3.3
Correlated with the residuals?
Add as factor to model, or b predict based on model score and stress test. Simple model, does it improve results?

