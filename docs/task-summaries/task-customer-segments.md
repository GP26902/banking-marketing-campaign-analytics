# Task Summary: Customer Segmentation Tab

**Project:** Banking Marketing Campaign Analytics Dashboard
**Deliverable:** New **🧩 Customer Segments** tab in `app.py` (fourth tab)
**Dataset:** UCI Bank Marketing dataset (`data/train.csv`), 45,211 customers

## 1. Objective

Combine two customer characteristics to find high- and low-response segments. A segment is one combination of the two chosen characteristics, for example *retired clients aged 65+*.

## 2. What Was Built

- **Two dropdowns** to choose the row and column characteristic from: age group, job, education, marital status, contact method, previous outcome.
- **Plotly heatmap** of the response rate for every combination. Hovering over a cell shows contacts, conversions and response rate.
- **Minimum segment size** setting (default 100 contacts). Segments below it are drawn grey on the heatmap and are excluded from the rankings.
- **Top 10 and bottom 10 tables** with contacts, conversions, response rate and lift versus the overall rate.
- **Sidebar filters** (job, age group, education, contact method, previous outcome) apply to everything in the tab. If no records match, the tab shows a warning instead of an error.

![Customer Segments tab](screenshots/customer-segments-tab.png)

## 3. Acceptance Criteria

| Criterion | Status | How it was checked |
|---|---|---|
| Heatmap works for any pair of the 6 characteristics | ✅ Done | Run for all 30 row/column combinations on the full dataset with no errors, plus manual clicking in the app. Choosing the same characteristic twice shows a message asking for two different ones. |
| Segments below the minimum size never appear in the top or bottom lists | ✅ Done | Rankings only use segments with `Contacts >= minimum size`. Verified at minimum sizes of 100 and 300. |
| Three spot-checked segment rates match a pandas calculation on `data/train.csv` | ✅ Done | See the table below. All three matched exactly. |
| Task summary lists the top 5 segments on the full dataset, with caveats | ✅ Done | Sections 5 and 6. |

### Spot checks (Job × Age group, no sidebar filters)

| Segment | Contacts | Conversions | Response Rate | Matches pandas |
|---|---:|---:|---:|---|
| retired, 65+ | 675 | 294 | 43.56% | ✅ |
| student, <25 | 327 | 117 | 35.78% | ✅ |
| blue-collar, 35-49 | 4,894 | 322 | 6.58% | ✅ |

## 4. Definitions

- **Response rate** = conversions ÷ contacts × 100 for the segment.
- **Lift** = segment response rate ÷ overall response rate. A lift of 2.0x means the segment responds at twice the average. The overall rate is calculated from the currently filtered data (11.70% with no filters applied).
- **Ranking:** segments are sorted by response rate. Ties are broken by number of contacts, with larger segments first.

## 5. Top 5 Segments on the Full Dataset

Pair: **Job × Age group**, minimum segment size 100, no sidebar filters. Overall response rate: 11.70%. 35 segments meet the minimum size.

| Rank | Segment | Contacts | Conversions | Response Rate | Lift |
|---|---|---:|---:|---:|---:|
| 1 | retired, 65+ | 675 | 294 | 43.56% | 3.72x |
| 2 | student, <25 | 327 | 117 | 35.78% | 3.06x |
| 3 | student, 25-34 | 549 | 135 | 24.59% | 2.10x |
| 4 | self-employed, 25-34 | 493 | 84 | 17.04% | 1.46x |
| 5 | unemployed, 50-64 | 296 | 49 | 16.55% | 1.41x |

**Pattern:** the highest-response segments are retired clients aged 65+ and students, especially under 25. Retired clients aged 35-49 (129 contacts, 3.10%) and blue-collar clients aged 35-49 and 50-64 are among the lowest.

**Other pairs:** when all 15 pairs of characteristics were checked, the top segments were dominated by clients with a previously successful campaign (previous outcome = success), at roughly 65-72% response. For example, retired + success converts at 71.84% on 174 contacts. This is consistent with the earlier campaign EDA, which found past success to be the strongest signal.

## 6. Caveats

- **These are associations, not causes.** A high response rate in a segment does not show that the characteristics caused the response.
- **Top segments are small.** Rank 1 has 675 contacts and rank 5 has 296, so their rates are less stable than those of large segments.
- **The minimum size changes the rankings.** The default of 100 contacts is a choice, not a statistical rule. A higher minimum removes smaller segments from the lists.
- **Segments overlap across pairs.** A client appears in one segment for each pair of characteristics, so results from different pairs should not be added together.
- **Some combinations have no customers.** These appear blank on the heatmap, which is different from the grey cells below the minimum size.
- **Fewer than 20 eligible segments.** When this happens, the top 10 and bottom 10 lists can overlap. The tab shows a note when this is the case.

## 7. Notes

- All existing behavior is unchanged: the five sidebar filters, KPI cards, and the first three tabs.
- New code in `app.py`: helper functions (`segment_summary`, `build_segment_heatmap`, `rank_segments`, `category_order`), a `SEGMENT_DIMENSIONS` mapping, and the `tab_segments` block. Two imports were added: `numpy` and `plotly.graph_objects`. `requirements.txt` is unchanged because `numpy` is installed with `pandas`.

## 8. Next Steps (Suggested)

- Check whether the strongest segments still stand out after controlling for other client characteristics.
- Consider allowing three-way segments, or adding a segment size column to the heatmap hover for easier comparison.
- Confirm with the marketing team which minimum segment size is acceptable for their decisions.
