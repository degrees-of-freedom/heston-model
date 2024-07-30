## 🚀 MJOLNIR (Python)

---

### ⚡ Feature Engineering (Feng)

---

**[GLOSS]:**

1. **Feature(s) derived from event variables**

   - **1.01) [DONE]:** Dummy variable(s) (scheduled event variable(s)),
   - **1.02) [DONE]:** Time-in-event (scheduled event variable(s)),
   - **1.03) [DONE]:** Time-to-event (scheduled event variable(s)),
   - **1.04) [DONE]:** Current surprise (actual - estimate) from event variable(s),
   - **1.05) [DONE]:** *Spread* between target' last surprise and peers average,

2. **Feature(s) derived from implied volatilities**

   - **2.01) [DONE]:** Implied volatilities **(ticker, base, maturity, delta, (dc,dp), last)**,
   - **2.02) [DONE]:** Implied volatilties *log-returns* {window} **(ticker, base, maturity, delta, (dc,dp), ret_{window})**, window ∈ (1d,1w,1m,3m),
   - **2.05) [DONE]:** Implied volatilties *endog, peers mean delta* **(med, base, maturity, delta, (dc,dp), last)**,
   - **2.06) [DONE]:** Implied volatilties *endog, peers mean delta* *returns* **(med, base, maturity, delta, (dc,dp), ret_{window})**, window ∈ (1d,1w,1m,3m),

3. **Feature(s) derived from implied volatilities *spreads***

   - **3.01) [DONE]:** Implied volatilities spreads **(ticker, spread, maturity, delta, nan, last)**,
   - **3.02) [DONE]:** Implied volatilties spreads *log-returns* {window} **(ticker, spread, maturity, delta, nan, ret_{window})**, window ∈ (1d,1w,1m,3m),
   - **3.05) [DONE]:** Implied volatilties spreads *endog, peers mean delta* **(med, spread, maturity, delta, nan, last)**,
   - **3.06) [DONE]:** Implied volatilties spreads *endog, peers mean delta* *returns* **(med, spread, maturity, delta, nan, ret_{window})**, window ∈ (1d,1w,1m,3m).

4. **Feature(s) derived from implied volatilities *skews***

   - **4.01) [DONE]:** Implied volatilities skews **(ticker, skew, maturity, delta, nan, last)**, delta ∈ (5,10,15),
   - **4.02) [DONE]:** Implied volatilties skews *log-returns* {window} **(ticker, skew, maturity, delta, nan, ret_{window})**, window ∈ (1d,1w,1m,3m) and delta ∈ (5,10,15),
   - **4.05) [DONE]:** Implied volatilties skews *endog, peers mean delta* **(med, skew, maturity, delta, nan, last)**, delta ∈ (5,10,15),
   - **4.06) [DONE]:** Implied volatilties skews *endog, peers mean delta* *returns* **(med, skew, maturity, delta, nan, ret_{window})**, window ∈ (1d,1w,1m,3m) and delta ∈ (5,10,15).

5. **Feature(s) derived from forward implied volatilities (term structure)**

   - **5.01) [DONE]:** Forward implied volatilities **(ticker, fwdv, (maturity_0, maturity_1), delta, (dc,dp), last)**,
   - **5.02) [DONE]:** Forward implied volatilties *log-returns* {window} **(ticker, fwdv, (maturity_0, maturity_1), delta, (dc,dp), ret_{window})**, window ∈ (1d,1w,1m,3m),
   - **5.05) [DONE]:** Forward implied volatilties *endog, peers mean delta* **(med, fwdv, (maturity_0, maturity_1), delta, (dc,dp), last)**,
   - **5.06) [DONE]:** Forward implied volatilties *endog, peers mean delta* *returns* **(med, fwdv, (maturity_0, maturity_1), delta, (dc,dp), ret_{window})**, window ∈ (1d,1w,1m,3m).

6. **Feature(s) derived from implied volatilities and realized volatilities *spreads***

   - **6.01) [DONE]:** Historical/Implied volatility spreads **(ticker, maturity, delta, rvs, last)**, delta = 50,
   - **6.02) [DONE]:** Historical/Implied volatility spreads *log-returns* {window} **(ticker, maturity, delta, rvs, ret_{window})**, window ∈ (1d,1w,1m,3m) and delta = 50,
   - **6.05) [DONE]:** Historical/Implied volatility spreads *endog, peers mean delta* **(med, maturity, delta, rvs, last)**, delta = 50,
   - **6.06) [DONE]:** Historical/Implied volatility spreads *endog, peers mean delta* *returns* **(med, maturity, delta, rvs, ret_{window})**, window ∈ (1d,1w,1m,3m) and delta = 50.

7. **Feature(s) derived from quotes**
   - **7.01) [DONE]:** Quotes **(ticker, close, last)**, 
   - **7.02) [DONE]:** Quotes *log-returns* {window} **(ticker, close, ret_{window})**, window ∈ (1d,1w,1m,3m)
   - **7.03) [DONE]:** Quotes *endog, peers mean delta* **(med, close, last)**.
   - **7.04) [DONE]:** Quotes *endog, peers mean delta* *returns* **(med, close, ret_{window})**, window ∈ (1d,1w,1m,3m).

8. **Feature(s) derived from technical variable(s)**
   - **8.01) [DONE]:** Volume-weighted average price (VWAP) **(ticker, vwap, last)**,
   - **8.02) [DONE]:** Volume-weighted average price (VWAP) *log-returns* {window}**(ticker, vwap, ret_{window})**, window ∈ (1d,1w,1m,3m),
   - **8.03) [DONE]:** Volume-weighted average price (VWAP) *endog, peers mean delta* **(med, vwap, last)**,
   - **8.04) [DONE]:** Volume-weighted average price (VWAP) *endog, peers mean delta* *log-returns* {window} **(med, vwap, ret_{window})**, window ∈ (1d,1w,1m,3m),
   - **8.05) [DONE]:** Average True Range (ATR) **(ticker, atr, last)**,
   - **8.06) [DONE]:** Average True Range (ATR) *log-returns* {window}**(ticker, atr, ret_{window})**, window ∈ (1d,1w,1m,3m),
   - **8.07) [DONE]:** Average True Range (ATR) *endog, peers mean delta* **(med, atr, last)**,
   - **8.08) [DONE]:** Average True Range (ATR) *endog, peers mean delta* *log-returns* {window} **(med, atr, ret_{window})**, window ∈ (1d,1w,1m,3m),
   - **8.09) [DONE]:** Relative Strength Index (RSI) **(ticker, rsi, last)**,
   - **8.10) [DONE]:** Relative Strength Index (RSI) *log-returns* {window}**(ticker, rsi, ret_{window})**, window ∈ (1d,1w,1m,3m),
   - **8.11) [DONE]:** Relative Strength Index (RSI) *endog, peers mean delta* **(med, rsi, last)**,
   - **8.12) [DONE]:** Relative Strength Index (RSI) *endog, peers mean delta* *log-returns* {window} **(med, rsi, ret_{window})**, window ∈ (1d,1w,1m,3m),
   - **8.13) [TODO]:** Rolling beta **(ticker, beta, last)**,
   - **8.14) [TODO]:** Relative Strength Index (RSI) *log-returns* {window}**(ticker, beta, ret_{window})**, window ∈ (1d,1w,1m,3m),
   - **8.15) [TODO]:** Rolling beta *endog, peers mean delta* **(med, beta, last)**,
   - **8.16) [TODO]:** Volume-weighted average price (VWAP) *endog, peers mean delta* *log-returns* {window} **(med, beta, ret_{window})**, window ∈ (1d,1w,1m,3m),

9. **Feature(s) derived from *moving correlations***
   -  **9.01) [DONE]:** Quote (last) *moving correlation* endog v. peers **(endog, ticker, mcorr_{window}, last)**.
 
1. **Feature(s) derived from consensus variables**
   - **10.01) [DONE]:** Consensus variables **(ticker, name, last)**,
   - **10.02) [DONE]:** Consensus variables *log-returns* **(ticker, name, ret_{window})**, window ∈ (1d,1w,1m,3m),
   - **10.05) [DONE]:** Consensus variables *endog, peers mean delta* **(med, name, last)**,
   - **10.06) [TODO]:** Consensus variables *endog, peers mean delta* *returns* **(med, name, ret_{window})**, window ∈ (1d,1w,1m,3m).

1. **Feature(s) derived throgh *zscores* transformations**
   - **10.01) [DONE]:** Implied volatilities *zscores* **(ticker, maturity, delta, (dc,dp), zscore)**,
   - **10.02) [DONE]:** Implied volatilties endog, peers mean delta *zscores* **(med, maturity, delta, (dc,dp), zscore)**,
   - **10.03) [DONE]:** Implied volatilities spreads *zscores* **(ticker, maturity, delta, spread, zscore)**,
   - **10.04) [DONE]:** Implied volatilties spreads endog, peers mean delta *zscores* **(med, maturity, delta, spread, zscore)**,
   - **10.05) [DONE]:** Implied volatilities skews *zscores* **(ticker, skew, maturity, delta, nan, zscore)**, delta ∈ (5,10,15),
   - **10.06) [DONE]:** Implied volatilties skews endog, peers mean delta *zscores* **(med, skew, maturity, delta, nan, zscore)**, delta ∈ (5,10,15),
   - **10.05) [TODO]:** Forward implied volatilities skews *zscores* **(ticker, maturity_0, maturity_1, delta, skew, zscore)**,
   - **10.06) [TODO]:** Forward implied volatilties skews endog, peers mean delta *zscores* **(med, maturity_0, maturity_1, delta, skew, zscore)**,
   - **10.07) [DONE]:** Historical/Implied volatility spreads *zscores* **(ticker, maturity, delta, rvs, zscore)**, delta = 50,
   - **10.08) [DONE]:** Historical/Implied volatility spreads endog, peers mean delta *zscores* **(med, maturity, delta, rvs, zscore)**, delta = 50,
   - **10.09) [DONE]:** Quote (last) moving correlation endog v. peers *zscores* **(endog, ticker, mcorr_{window}, zscore)**,
   - **10.10) [DONE]:** Implied volatilities moving correlation endog v. vix index *zscores* **(endog, vix, mcorr_{window}, zscore)**,
   - **10.11) [DONE]:** Consensus variables *zscores* **(ticker, name, zscore)**,
   - **10.12) [DONE]:** Consensus variables endog, peers mean delta *zscores* **(med, name, zscore)**,
   - **10.13) [TODO]:** Volume-weighted average price (VWAP) *zscores***(ticker, vwap, zscore)**,
   - **10.14) [TODO]:** Volume-weighted average price (VWAP) *endog, peers mean delta* *zscores* **(med, vwap, zscore)**,
   - **10.15) [TODO]:** Rolling beta *zscores* **(ticker, beta, zscore)**,
   - **10.16) [TODO]:** Rolling beta *endog, peers mean delta* *zscores* **(med, beta, zscore)**,
