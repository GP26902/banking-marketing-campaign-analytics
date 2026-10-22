# Campaign response rates by campaign characteristics

Dataset: `data/train.csv` (45,211 records). A positive response is `y = yes`, meaning the customer subscribed to a term deposit. For each segment, response rate = positive responses / records in the segment × 100. Calculations use the original semicolon-delimited file and retain `unknown` values as their own categories.

**Overall:** 5,289 of 45,211 customers responded positively (**11.70%**).

## Contact method

| Contact method | Records | Positive responses | Response rate |
| --- | ---: | ---: | ---: |
| Cellular | 29,285 | 4,369 | 14.92% |
| Telephone | 2,906 | 390 | 13.42% |
| Unknown | 13,020 | 530 | 4.07% |

Cellular has the highest observed rate, 1.50 percentage points above telephone. Records with unknown contact method have a much lower observed rate; this label is missing channel information, not a third known channel.

## Contacts in current campaign

| Contact attempts | Records | Positive responses | Response rate |
| --- | ---: | ---: | ---: |
| 1 | 17,544 | 2,561 | 14.60% |
| 2 | 12,505 | 1,401 | 11.20% |
| 3 | 5,521 | 618 | 11.19% |
| 4 | 3,522 | 317 | 9.00% |
| 5-10 | 4,923 | 345 | 7.01% |
| 11+ | 1,196 | 47 | 3.93% |

The observed response rate declines across these groups, from 14.60% for one contact to 3.93% for 11 or more, a 10.67 percentage-point drop. This pattern does not establish that extra calls cause lower response: harder-to-convert customers may receive more calls.

## Previous campaign outcome

| Previous outcome | Records | Positive responses | Response rate |
| --- | ---: | ---: | ---: |
| Success | 1,511 | 978 | 64.73% |
| Other | 1,840 | 307 | 16.68% |
| Failure | 4,901 | 618 | 12.61% |
| Unknown | 36,959 | 3,386 | 9.16% |

Customers with a recorded previous success have the highest observed response rate, 55.57 percentage points above records with unknown previous outcome. `Unknown` includes records without a known prior outcome and must not be described as a previous failure.

## Initial insights

1. Known cellular contacts show a modestly higher response rate than telephone contacts.
2. Segments with fewer contacts in the current campaign show higher response rates, though this is descriptive rather than causal.
3. A recorded previous success is strongly associated with a positive response in this dataset. Its group is much smaller than the unknown-outcome group, so both counts and rates should be shown.

## Reproduction

```python
import pandas as pd

df = pd.read_csv('data/train.csv', sep=';')
df['positive'] = df['y'].eq('yes').astype(int)
df['contact_attempts'] = pd.cut(
    df['campaign'], bins=[0, 1, 2, 3, 4, 10, float('inf')],
    labels=['1', '2', '3', '4', '5-10', '11+']
)
for characteristic in ['contact', 'contact_attempts', 'poutcome']:
    result = df.groupby(characteristic, observed=True)['positive'].agg(
        records='size', positive_responses='sum', response_rate='mean'
    )
    result['response_rate'] *= 100
    print(characteristic, result.round(2), sep='\n')
```