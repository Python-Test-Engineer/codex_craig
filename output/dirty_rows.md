# Dirty Row Report

- **Total rows in dataset:** 2823
- **Dirty rows identified:** 2679
- **Clean rows:** 144

## Criteria Used

A row is flagged as **dirty** if it satisfies one or more of the following conditions:

| # | Criterion | Description |
|---|-----------|-------------|
| 1 | **Missing value** | One or more cells are null / NaN |
| 2 | **Exact duplicate** | Row is an identical copy of an earlier row |
| 3 | **Numeric outlier** | A numeric value falls outside +/- 3 standard deviations from the column mean |
| 4 | **Negative in non-negative column** | A numeric value is negative in a column whose name implies non-negative values (price, quantity, total, etc.) |

## Summary by Criterion

- **Missing values:** 2676 row(s)
- **Numeric outliers (+/-3 std dev):** 39 row(s)

## Row-by-Row Detail

### Row 0
- Missing value(s) in column(s): addressline2, territory

### Row 1
- Missing value(s) in column(s): addressline2, state

### Row 2
- Missing value(s) in column(s): addressline2, state

### Row 3
- Missing value(s) in column(s): addressline2, territory

### Row 4
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 5
- Missing value(s) in column(s): addressline2, territory

### Row 6
- Missing value(s) in column(s): addressline2, state

### Row 7
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 8
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 9
- Missing value(s) in column(s): addressline2, state

### Row 11
- Missing value(s) in column(s): territory

### Row 12
- Missing value(s) in column(s): addressline2, territory

### Row 13
- Missing value(s) in column(s): addressline2, territory

### Row 14
- Missing value(s) in column(s): addressline2, state

### Row 15
- Missing value(s) in column(s): addressline2, territory

### Row 16
- Missing value(s) in column(s): addressline2, state

### Row 17
- Missing value(s) in column(s): addressline2, state

### Row 18
- Missing value(s) in column(s): addressline2, territory

### Row 19
- Missing value(s) in column(s): addressline2, territory

### Row 20
- Missing value(s) in column(s): addressline2, state

### Row 22
- Missing value(s) in column(s): addressline2, state

### Row 23
- Missing value(s) in column(s): addressline2, territory

### Row 24
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 25
- Missing value(s) in column(s): addressline2, state
- Outlier in 'quantityordered': 66 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])

### Row 26
- Missing value(s) in column(s): addressline2, state

### Row 27
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 28
- Missing value(s) in column(s): addressline2, state

### Row 29
- Missing value(s) in column(s): addressline2, territory

### Row 30
- Missing value(s) in column(s): addressline2, state
- Outlier in 'sales': 1.099e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 31
- Missing value(s) in column(s): territory

### Row 32
- Missing value(s) in column(s): addressline2

### Row 33
- Missing value(s) in column(s): addressline2, territory

### Row 34
- Missing value(s) in column(s): addressline2, state

### Row 35
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 36
- Missing value(s) in column(s): addressline2, territory

### Row 37
- Missing value(s) in column(s): addressline2, territory

### Row 38
- Missing value(s) in column(s): addressline2, territory

### Row 39
- Missing value(s) in column(s): addressline2, postalcode

### Row 41
- Missing value(s) in column(s): addressline2, state

### Row 42
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 43
- Missing value(s) in column(s): addressline2, state
- Outlier in 'sales': 1.017e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 44
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'sales': 1.162e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 45
- Missing value(s) in column(s): addressline2, territory

### Row 46
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 48
- Missing value(s) in column(s): addressline2, territory

### Row 49
- Missing value(s) in column(s): addressline2, territory

### Row 50
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 52
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 53
- Missing value(s) in column(s): addressline2, state
- Outlier in 'sales': 1.2e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 54
- Missing value(s) in column(s): addressline2, territory

### Row 56
- Missing value(s) in column(s): addressline2, state

### Row 57
- Missing value(s) in column(s): addressline2, territory

### Row 58
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 59
- Missing value(s) in column(s): addressline2, territory

### Row 60
- Missing value(s) in column(s): addressline2, state

### Row 61
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 62
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 63
- Missing value(s) in column(s): addressline2, postalcode

### Row 65
- Missing value(s) in column(s): addressline2, territory

### Row 66
- Missing value(s) in column(s): addressline2, territory

### Row 67
- Missing value(s) in column(s): addressline2, territory

### Row 68
- Missing value(s) in column(s): addressline2, state

### Row 69
- Missing value(s) in column(s): addressline2, territory

### Row 70
- Missing value(s) in column(s): addressline2, state

### Row 71
- Missing value(s) in column(s): addressline2, territory

### Row 72
- Missing value(s) in column(s): addressline2, territory

### Row 73
- Missing value(s) in column(s): addressline2, territory

### Row 74
- Missing value(s) in column(s): addressline2, postalcode

### Row 76
- Missing value(s) in column(s): addressline2

### Row 77
- Missing value(s) in column(s): addressline2, territory

### Row 78
- Missing value(s) in column(s): addressline2, state

### Row 79
- Missing value(s) in column(s): addressline2, state

### Row 80
- Missing value(s) in column(s): addressline2, territory

### Row 81
- Outlier in 'sales': 9265 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 82
- Missing value(s) in column(s): addressline2, state

### Row 83
- Missing value(s) in column(s): addressline2, territory

### Row 84
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 85
- Missing value(s) in column(s): addressline2, territory

### Row 86
- Missing value(s) in column(s): addressline2, state

### Row 87
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 88
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 89
- Missing value(s) in column(s): addressline2, postalcode

### Row 90
- Outlier in 'sales': 9774 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 91
- Missing value(s) in column(s): territory

### Row 92
- Missing value(s) in column(s): addressline2, territory

### Row 93
- Missing value(s) in column(s): addressline2, territory

### Row 94
- Missing value(s) in column(s): addressline2, state

### Row 95
- Missing value(s) in column(s): addressline2, territory

### Row 96
- Missing value(s) in column(s): addressline2, state

### Row 97
- Missing value(s) in column(s): addressline2, territory

### Row 98
- Missing value(s) in column(s): addressline2, territory

### Row 99
- Missing value(s) in column(s): addressline2, territory

### Row 100
- Missing value(s) in column(s): addressline2, postalcode

### Row 101
- Missing value(s) in column(s): addressline2, territory

### Row 102
- Missing value(s) in column(s): addressline2

### Row 103
- Missing value(s) in column(s): addressline2, territory

### Row 104
- Missing value(s) in column(s): addressline2, state, postalcode
- Outlier in 'quantityordered': 66 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])
- Outlier in 'sales': 1.189e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 105
- Missing value(s) in column(s): addressline2, state
- Outlier in 'sales': 9218 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 106
- Missing value(s) in column(s): addressline2, state

### Row 107
- Missing value(s) in column(s): addressline2, state

### Row 108
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 109
- Missing value(s) in column(s): addressline2, territory

### Row 110
- Missing value(s) in column(s): addressline2, state

### Row 111
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 112
- Missing value(s) in column(s): addressline2, state

### Row 113
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 114
- Missing value(s) in column(s): addressline2, state

### Row 115
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 116
- Missing value(s) in column(s): addressline2, territory

### Row 117
- Missing value(s) in column(s): addressline2, territory

### Row 118
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 119
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 120
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 121
- Missing value(s) in column(s): addressline2, territory

### Row 122
- Missing value(s) in column(s): addressline2, territory

### Row 123
- Missing value(s) in column(s): addressline2, postalcode

### Row 124
- Missing value(s) in column(s): addressline2, state

### Row 125
- Missing value(s) in column(s): territory

### Row 126
- Missing value(s) in column(s): addressline2, state

### Row 127
- Missing value(s) in column(s): addressline2, state

### Row 128
- Missing value(s) in column(s): addressline2, state

### Row 129
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 130
- Missing value(s) in column(s): addressline2, state

### Row 131
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'sales': 9661 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 132
- Missing value(s) in column(s): addressline2, territory

### Row 133
- Missing value(s) in column(s): addressline2, state

### Row 134
- Missing value(s) in column(s): addressline2, state

### Row 135
- Missing value(s) in column(s): addressline2, state

### Row 136
- Missing value(s) in column(s): addressline2, territory

### Row 137
- Missing value(s) in column(s): addressline2, state

### Row 138
- Missing value(s) in column(s): addressline2, state

### Row 139
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 140
- Missing value(s) in column(s): addressline2, territory

### Row 141
- Missing value(s) in column(s): addressline2, state

### Row 142
- Missing value(s) in column(s): addressline2, territory

### Row 143
- Missing value(s) in column(s): state

### Row 144
- Missing value(s) in column(s): addressline2, territory

### Row 145
- Missing value(s) in column(s): addressline2, territory

### Row 146
- Missing value(s) in column(s): state

### Row 148
- Missing value(s) in column(s): addressline2, territory

### Row 149
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 150
- Missing value(s) in column(s): addressline2, territory

### Row 151
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 152
- Missing value(s) in column(s): addressline2, territory

### Row 153
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 155
- Missing value(s) in column(s): addressline2, territory

### Row 157
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 159
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 160
- Missing value(s) in column(s): addressline2, state

### Row 161
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 162
- Missing value(s) in column(s): addressline2, state

### Row 163
- Missing value(s) in column(s): addressline2, territory

### Row 164
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'sales': 9246 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 165
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 167
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 168
- Missing value(s) in column(s): addressline2, state

### Row 169
- Missing value(s) in column(s): addressline2, state

### Row 170
- Missing value(s) in column(s): addressline2, state

### Row 171
- Missing value(s) in column(s): addressline2, state

### Row 172
- Missing value(s) in column(s): addressline2, state

### Row 173
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 174
- Missing value(s) in column(s): addressline2, state
- Outlier in 'sales': 9160 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 175
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'sales': 9631 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 176
- Missing value(s) in column(s): addressline2, state

### Row 177
- Missing value(s) in column(s): addressline2, state

### Row 178
- Missing value(s) in column(s): addressline2, state

### Row 179
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 180
- Missing value(s) in column(s): addressline2, territory

### Row 181
- Missing value(s) in column(s): addressline2, state

### Row 182
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 183
- Missing value(s) in column(s): addressline2, state

### Row 184
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 185
- Missing value(s) in column(s): addressline2, state

### Row 186
- Missing value(s) in column(s): addressline2, state

### Row 187
- Missing value(s) in column(s): addressline2, state

### Row 188
- Missing value(s) in column(s): territory
- Outlier in 'sales': 1.128e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 189
- Missing value(s) in column(s): addressline2, territory

### Row 190
- Missing value(s) in column(s): addressline2, state

### Row 191
- Missing value(s) in column(s): addressline2, state

### Row 192
- Missing value(s) in column(s): addressline2, state

### Row 193
- Missing value(s) in column(s): addressline2, territory

### Row 194
- Missing value(s) in column(s): addressline2, territory

### Row 195
- Missing value(s) in column(s): addressline2, state

### Row 196
- Missing value(s) in column(s): state

### Row 197
- Missing value(s) in column(s): addressline2, state

### Row 198
- Missing value(s) in column(s): addressline2, state, postalcode
- Outlier in 'sales': 1.061e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 199
- Missing value(s) in column(s): addressline2, territory

### Row 200
- Missing value(s) in column(s): addressline2, territory

### Row 201
- Missing value(s) in column(s): addressline2, state

### Row 202
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 203
- Missing value(s) in column(s): addressline2, state

### Row 204
- Missing value(s) in column(s): addressline2, state

### Row 205
- Missing value(s) in column(s): addressline2, state

### Row 206
- Missing value(s) in column(s): addressline2, state

### Row 207
- Missing value(s) in column(s): addressline2, state

### Row 208
- Missing value(s) in column(s): addressline2, territory

### Row 209
- Missing value(s) in column(s): addressline2, territory

### Row 210
- Missing value(s) in column(s): addressline2, state

### Row 211
- Missing value(s) in column(s): addressline2, territory

### Row 212
- Missing value(s) in column(s): addressline2, state

### Row 213
- Missing value(s) in column(s): addressline2, territory

### Row 214
- Missing value(s) in column(s): addressline2, state

### Row 215
- Missing value(s) in column(s): addressline2, territory

### Row 216
- Missing value(s) in column(s): addressline2, state

### Row 217
- Missing value(s) in column(s): addressline2, state

### Row 218
- Missing value(s) in column(s): addressline2

### Row 219
- Missing value(s) in column(s): addressline2, territory

### Row 220
- Missing value(s) in column(s): addressline2, state

### Row 221
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 222
- Missing value(s) in column(s): addressline2, state

### Row 223
- Missing value(s) in column(s): addressline2, territory

### Row 224
- Missing value(s) in column(s): addressline2, territory

### Row 225
- Missing value(s) in column(s): addressline2, postalcode

### Row 227
- Missing value(s) in column(s): addressline2, territory

### Row 228
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 229
- Missing value(s) in column(s): addressline2, state

### Row 230
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 231
- Missing value(s) in column(s): addressline2, territory

### Row 232
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 234
- Missing value(s) in column(s): addressline2, territory

### Row 236
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 238
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 239
- Missing value(s) in column(s): addressline2, state

### Row 240
- Missing value(s) in column(s): addressline2, territory

### Row 241
- Missing value(s) in column(s): addressline2, state

### Row 242
- Missing value(s) in column(s): addressline2, state

### Row 243
- Missing value(s) in column(s): addressline2, territory

### Row 244
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 246
- Missing value(s) in column(s): addressline2, state

### Row 247
- Missing value(s) in column(s): addressline2, territory

### Row 248
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 249
- Missing value(s) in column(s): addressline2, state

### Row 250
- Missing value(s) in column(s): addressline2, state

### Row 251
- Missing value(s) in column(s): territory

### Row 252
- Missing value(s) in column(s): addressline2, territory

### Row 253
- Missing value(s) in column(s): addressline2, territory

### Row 254
- Missing value(s) in column(s): addressline2, territory

### Row 255
- Missing value(s) in column(s): addressline2, territory

### Row 256
- Missing value(s) in column(s): addressline2, state

### Row 257
- Missing value(s) in column(s): addressline2, state

### Row 258
- Missing value(s) in column(s): territory

### Row 259
- Missing value(s) in column(s): addressline2, territory

### Row 260
- Missing value(s) in column(s): addressline2, state

### Row 261
- Missing value(s) in column(s): addressline2, territory

### Row 262
- Missing value(s) in column(s): addressline2, state

### Row 263
- Missing value(s) in column(s): addressline2, territory

### Row 264
- Missing value(s) in column(s): addressline2, state, postalcode
- Outlier in 'quantityordered': 66 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])

### Row 265
- Missing value(s) in column(s): addressline2, state

### Row 266
- Missing value(s) in column(s): addressline2, state

### Row 267
- Missing value(s) in column(s): addressline2, state

### Row 268
- Missing value(s) in column(s): territory

### Row 269
- Missing value(s) in column(s): addressline2, territory

### Row 270
- Missing value(s) in column(s): addressline2, state

### Row 271
- Missing value(s) in column(s): addressline2, state

### Row 272
- Missing value(s) in column(s): addressline2, state

### Row 273
- Missing value(s) in column(s): addressline2, territory

### Row 274
- Missing value(s) in column(s): addressline2, territory

### Row 275
- Missing value(s) in column(s): addressline2, state

### Row 276
- Missing value(s) in column(s): state

### Row 277
- Missing value(s) in column(s): addressline2, state

### Row 278
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 279
- Missing value(s) in column(s): addressline2, territory

### Row 280
- Missing value(s) in column(s): addressline2, territory

### Row 281
- Missing value(s) in column(s): addressline2, state

### Row 282
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 283
- Missing value(s) in column(s): addressline2, state

### Row 284
- Missing value(s) in column(s): territory

### Row 285
- Missing value(s) in column(s): addressline2, state

### Row 286
- Missing value(s) in column(s): addressline2, state

### Row 287
- Missing value(s) in column(s): addressline2, state

### Row 288
- Missing value(s) in column(s): addressline2, postalcode

### Row 289
- Missing value(s) in column(s): addressline2, territory

### Row 290
- Missing value(s) in column(s): addressline2, territory

### Row 291
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 292
- Missing value(s) in column(s): addressline2, state

### Row 293
- Missing value(s) in column(s): addressline2, territory

### Row 294
- Missing value(s) in column(s): addressline2, territory

### Row 295
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 296
- Missing value(s) in column(s): addressline2, state

### Row 297
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 298
- Missing value(s) in column(s): addressline2, state

### Row 299
- Missing value(s) in column(s): addressline2, state

### Row 300
- Missing value(s) in column(s): addressline2, state

### Row 301
- Missing value(s) in column(s): addressline2, state

### Row 302
- Missing value(s) in column(s): addressline2, state

### Row 303
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 304
- Missing value(s) in column(s): addressline2, state

### Row 305
- Missing value(s) in column(s): addressline2, territory

### Row 306
- Missing value(s) in column(s): addressline2, state

### Row 307
- Missing value(s) in column(s): addressline2, state

### Row 308
- Missing value(s) in column(s): addressline2, state

### Row 309
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 310
- Missing value(s) in column(s): addressline2, territory

### Row 311
- Missing value(s) in column(s): addressline2, state

### Row 312
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 313
- Missing value(s) in column(s): addressline2, territory

### Row 314
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 315
- Missing value(s) in column(s): addressline2, state

### Row 316
- Missing value(s) in column(s): addressline2, state

### Row 317
- Missing value(s) in column(s): addressline2, state

### Row 318
- Missing value(s) in column(s): territory

### Row 319
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'sales': 9471 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 320
- Missing value(s) in column(s): addressline2, state

### Row 321
- Missing value(s) in column(s): addressline2, state

### Row 322
- Missing value(s) in column(s): addressline2, state

### Row 323
- Missing value(s) in column(s): addressline2, territory

### Row 324
- Missing value(s) in column(s): addressline2, territory

### Row 325
- Missing value(s) in column(s): addressline2, state

### Row 326
- Missing value(s) in column(s): state

### Row 327
- Missing value(s) in column(s): addressline2, state

### Row 328
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 329
- Missing value(s) in column(s): addressline2, territory

### Row 330
- Missing value(s) in column(s): addressline2, territory

### Row 331
- Missing value(s) in column(s): addressline2, state

### Row 332
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 333
- Missing value(s) in column(s): addressline2, state

### Row 334
- Missing value(s) in column(s): addressline2, state

### Row 335
- Missing value(s) in column(s): addressline2, state

### Row 336
- Missing value(s) in column(s): territory

### Row 337
- Missing value(s) in column(s): addressline2, state

### Row 338
- Missing value(s) in column(s): addressline2, postalcode

### Row 339
- Missing value(s) in column(s): addressline2, territory

### Row 340
- Missing value(s) in column(s): addressline2, territory

### Row 341
- Missing value(s) in column(s): addressline2, territory

### Row 342
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 343
- Missing value(s) in column(s): addressline2, state

### Row 344
- Missing value(s) in column(s): addressline2, territory

### Row 345
- Missing value(s) in column(s): addressline2, territory

### Row 346
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 348
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 349
- Missing value(s) in column(s): addressline2, state

### Row 350
- Missing value(s) in column(s): addressline2, state

### Row 351
- Missing value(s) in column(s): addressline2, state

### Row 352
- Missing value(s) in column(s): addressline2, state

### Row 353
- Missing value(s) in column(s): addressline2, state

### Row 354
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 355
- Missing value(s) in column(s): addressline2, state

### Row 356
- Missing value(s) in column(s): addressline2, territory

### Row 357
- Missing value(s) in column(s): addressline2, state

### Row 358
- Missing value(s) in column(s): addressline2, state

### Row 359
- Missing value(s) in column(s): addressline2, state

### Row 360
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 361
- Missing value(s) in column(s): addressline2, territory

### Row 362
- Missing value(s) in column(s): addressline2, state

### Row 363
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 364
- Missing value(s) in column(s): addressline2, state

### Row 365
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 366
- Missing value(s) in column(s): addressline2, state

### Row 367
- Missing value(s) in column(s): addressline2, state

### Row 368
- Missing value(s) in column(s): territory

### Row 369
- Missing value(s) in column(s): territory

### Row 370
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 371
- Missing value(s) in column(s): addressline2, state

### Row 372
- Missing value(s) in column(s): addressline2, state

### Row 373
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 374
- Missing value(s) in column(s): addressline2, state

### Row 375
- Missing value(s) in column(s): addressline2, territory

### Row 376
- Missing value(s) in column(s): addressline2, territory

### Row 377
- Missing value(s) in column(s): addressline2, territory

### Row 378
- Missing value(s) in column(s): addressline2, territory

### Row 379
- Missing value(s) in column(s): addressline2, state

### Row 380
- Missing value(s) in column(s): state

### Row 381
- Missing value(s) in column(s): addressline2, territory

### Row 382
- Missing value(s) in column(s): addressline2, territory

### Row 383
- Missing value(s) in column(s): addressline2, territory

### Row 384
- Missing value(s) in column(s): addressline2, territory

### Row 385
- Missing value(s) in column(s): addressline2, state

### Row 386
- Missing value(s) in column(s): territory

### Row 387
- Missing value(s) in column(s): addressline2, state

### Row 388
- Missing value(s) in column(s): territory

### Row 389
- Missing value(s) in column(s): addressline2, state

### Row 390
- Missing value(s) in column(s): addressline2, territory

### Row 391
- Missing value(s) in column(s): addressline2, territory

### Row 392
- Missing value(s) in column(s): addressline2, state

### Row 393
- Missing value(s) in column(s): addressline2, state

### Row 394
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 395
- Missing value(s) in column(s): addressline2, state

### Row 396
- Missing value(s) in column(s): addressline2, territory

### Row 397
- Missing value(s) in column(s): addressline2, territory

### Row 398
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 399
- Missing value(s) in column(s): addressline2, state

### Row 400
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 401
- Missing value(s) in column(s): addressline2, territory

### Row 402
- Missing value(s) in column(s): addressline2, state

### Row 403
- Missing value(s) in column(s): addressline2, state

### Row 404
- Missing value(s) in column(s): addressline2, state

### Row 405
- Missing value(s) in column(s): addressline2, state

### Row 406
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 407
- Missing value(s) in column(s): addressline2, state

### Row 408
- Missing value(s) in column(s): addressline2, state

### Row 409
- Missing value(s) in column(s): addressline2, state

### Row 410
- Missing value(s) in column(s): addressline2, state

### Row 411
- Missing value(s) in column(s): addressline2, state

### Row 412
- Missing value(s) in column(s): addressline2, territory

### Row 413
- Missing value(s) in column(s): addressline2, territory

### Row 414
- Missing value(s) in column(s): addressline2, state

### Row 415
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 416
- Missing value(s) in column(s): addressline2, state

### Row 417
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 418
- Missing value(s) in column(s): addressline2, state
- Outlier in 'quantityordered': 97 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])

### Row 419
- Missing value(s) in column(s): addressline2, state

### Row 420
- Missing value(s) in column(s): addressline2, state

### Row 421
- Missing value(s) in column(s): addressline2, territory

### Row 422
- Missing value(s) in column(s): addressline2, state

### Row 423
- Missing value(s) in column(s): addressline2, territory

### Row 424
- Missing value(s) in column(s): addressline2, state

### Row 425
- Missing value(s) in column(s): addressline2, state

### Row 426
- Missing value(s) in column(s): addressline2

### Row 427
- Missing value(s) in column(s): addressline2, territory

### Row 428
- Missing value(s) in column(s): addressline2, state

### Row 429
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 430
- Missing value(s) in column(s): addressline2, territory

### Row 431
- Missing value(s) in column(s): addressline2, territory

### Row 432
- Missing value(s) in column(s): addressline2, territory

### Row 433
- Missing value(s) in column(s): addressline2, postalcode

### Row 435
- Missing value(s) in column(s): addressline2, state

### Row 436
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 437
- Missing value(s) in column(s): addressline2, state

### Row 438
- Missing value(s) in column(s): addressline2, territory

### Row 439
- Missing value(s) in column(s): addressline2, territory

### Row 440
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 442
- Missing value(s) in column(s): addressline2, territory

### Row 444
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 446
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 447
- Missing value(s) in column(s): addressline2, state

### Row 448
- Missing value(s) in column(s): addressline2, territory

### Row 449
- Missing value(s) in column(s): addressline2, state

### Row 450
- Missing value(s) in column(s): addressline2, state

### Row 452
- Missing value(s) in column(s): addressline2, state

### Row 453
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 454
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 455
- Missing value(s) in column(s): addressline2, territory

### Row 456
- Missing value(s) in column(s): territory

### Row 457
- Missing value(s) in column(s): addressline2, state

### Row 458
- Missing value(s) in column(s): addressline2, state

### Row 459
- Missing value(s) in column(s): addressline2, postalcode

### Row 460
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 461
- Missing value(s) in column(s): addressline2, state

### Row 462
- Missing value(s) in column(s): addressline2, territory

### Row 463
- Missing value(s) in column(s): addressline2, state

### Row 464
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 465
- Missing value(s) in column(s): addressline2, state

### Row 466
- Missing value(s) in column(s): addressline2, territory

### Row 467
- Missing value(s) in column(s): addressline2, territory

### Row 469
- Missing value(s) in column(s): addressline2, state

### Row 470
- Missing value(s) in column(s): addressline2, territory

### Row 471
- Missing value(s) in column(s): addressline2, state

### Row 472
- Missing value(s) in column(s): addressline2, territory

### Row 473
- Missing value(s) in column(s): addressline2, state

### Row 474
- Missing value(s) in column(s): addressline2, state

### Row 475
- Missing value(s) in column(s): territory

### Row 476
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 479
- Missing value(s) in column(s): addressline2, territory

### Row 480
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 481
- Missing value(s) in column(s): addressline2, state

### Row 482
- Missing value(s) in column(s): addressline2, territory

### Row 483
- Missing value(s) in column(s): addressline2

### Row 484
- Missing value(s) in column(s): addressline2, state

### Row 485
- Missing value(s) in column(s): addressline2, territory

### Row 486
- Missing value(s) in column(s): addressline2, state

### Row 487
- Missing value(s) in column(s): addressline2, state

### Row 488
- Missing value(s) in column(s): addressline2, state

### Row 489
- Missing value(s) in column(s): addressline2, state

### Row 490
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 491
- Missing value(s) in column(s): addressline2, state

### Row 492
- Missing value(s) in column(s): addressline2, territory

### Row 493
- Missing value(s) in column(s): addressline2, territory

### Row 494
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 495
- Missing value(s) in column(s): addressline2, territory

### Row 496
- Missing value(s) in column(s): addressline2, state

### Row 497
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'sales': 9240 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 498
- Missing value(s) in column(s): addressline2, state

### Row 500
- Missing value(s) in column(s): addressline2, territory

### Row 501
- Missing value(s) in column(s): territory

### Row 502
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 503
- Missing value(s) in column(s): addressline2, state

### Row 505
- Missing value(s) in column(s): addressline2, territory

### Row 506
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 507
- Missing value(s) in column(s): addressline2, state

### Row 508
- Missing value(s) in column(s): addressline2, territory

### Row 509
- Missing value(s) in column(s): addressline2

### Row 510
- Missing value(s) in column(s): addressline2, state

### Row 511
- Missing value(s) in column(s): addressline2, territory

### Row 512
- Missing value(s) in column(s): addressline2, state

### Row 513
- Missing value(s) in column(s): addressline2, state

### Row 514
- Missing value(s) in column(s): addressline2, state

### Row 515
- Missing value(s) in column(s): addressline2, state

### Row 516
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 517
- Missing value(s) in column(s): addressline2, state

### Row 518
- Missing value(s) in column(s): addressline2, territory

### Row 519
- Missing value(s) in column(s): addressline2, territory

### Row 520
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 522
- Missing value(s) in column(s): addressline2, state

### Row 523
- Missing value(s) in column(s): addressline2, territory

### Row 524
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 526
- Missing value(s) in column(s): addressline2, territory

### Row 527
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 528
- Missing value(s) in column(s): addressline2, state

### Row 529
- Missing value(s) in column(s): addressline2, state

### Row 531
- Missing value(s) in column(s): addressline2, state

### Row 532
- Missing value(s) in column(s): addressline2, territory

### Row 533
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 534
- Missing value(s) in column(s): addressline2, territory

### Row 535
- Missing value(s) in column(s): territory

### Row 536
- Missing value(s) in column(s): addressline2, state

### Row 537
- Missing value(s) in column(s): addressline2, territory

### Row 538
- Missing value(s) in column(s): addressline2, state

### Row 539
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 540
- Missing value(s) in column(s): addressline2, state

### Row 541
- Missing value(s) in column(s): addressline2, territory

### Row 542
- Missing value(s) in column(s): state

### Row 543
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 544
- Missing value(s) in column(s): addressline2, state

### Row 545
- Missing value(s) in column(s): addressline2, territory

### Row 546
- Missing value(s) in column(s): addressline2, territory

### Row 547
- Missing value(s) in column(s): addressline2, state

### Row 548
- Missing value(s) in column(s): addressline2, territory

### Row 549
- Missing value(s) in column(s): addressline2, state

### Row 550
- Missing value(s) in column(s): addressline2, territory

### Row 551
- Missing value(s) in column(s): addressline2, state

### Row 552
- Missing value(s) in column(s): addressline2, state

### Row 553
- Missing value(s) in column(s): addressline2, state

### Row 554
- Missing value(s) in column(s): addressline2, territory

### Row 555
- Missing value(s) in column(s): addressline2, territory

### Row 556
- Missing value(s) in column(s): addressline2, state

### Row 557
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 558
- Missing value(s) in column(s): addressline2, state

### Row 559
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 560
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 561
- Missing value(s) in column(s): addressline2, postalcode

### Row 562
- Missing value(s) in column(s): addressline2, territory

### Row 563
- Missing value(s) in column(s): addressline2, territory

### Row 564
- Missing value(s) in column(s): addressline2, state

### Row 565
- Missing value(s) in column(s): addressline2, territory

### Row 566
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 567
- Missing value(s) in column(s): addressline2, state

### Row 568
- Missing value(s) in column(s): addressline2, territory

### Row 569
- Missing value(s) in column(s): addressline2, postalcode

### Row 570
- Missing value(s) in column(s): addressline2, state

### Row 571
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 572
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 573
- Missing value(s) in column(s): addressline2, state

### Row 574
- Missing value(s) in column(s): addressline2, state

### Row 575
- Missing value(s) in column(s): addressline2, state

### Row 576
- Missing value(s) in column(s): addressline2, territory

### Row 577
- Missing value(s) in column(s): addressline2, state

### Row 578
- Missing value(s) in column(s): addressline2, territory

### Row 579
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 580
- Missing value(s) in column(s): addressline2, territory

### Row 581
- Missing value(s) in column(s): addressline2, territory

### Row 582
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 583
- Missing value(s) in column(s): addressline2, state

### Row 584
- Missing value(s) in column(s): addressline2, territory

### Row 585
- Missing value(s) in column(s): addressline2

### Row 586
- Missing value(s) in column(s): territory

### Row 587
- Missing value(s) in column(s): addressline2, state

### Row 588
- Missing value(s) in column(s): addressline2, state

### Row 589
- Missing value(s) in column(s): addressline2, state

### Row 590
- Missing value(s) in column(s): addressline2, state

### Row 591
- Missing value(s) in column(s): state

### Row 592
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 593
- Missing value(s) in column(s): addressline2, territory

### Row 594
- Missing value(s) in column(s): addressline2, territory

### Row 595
- Missing value(s) in column(s): addressline2, state

### Row 596
- Missing value(s) in column(s): addressline2, territory

### Row 597
- Missing value(s) in column(s): addressline2, state

### Row 598
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'quantityordered': 76 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])
- Outlier in 'sales': 1.408e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 600
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 601
- Missing value(s) in column(s): addressline2, state

### Row 602
- Missing value(s) in column(s): addressline2, territory

### Row 603
- Missing value(s) in column(s): addressline2, territory

### Row 604
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 605
- Missing value(s) in column(s): addressline2, state

### Row 606
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 607
- Missing value(s) in column(s): addressline2, territory

### Row 608
- Missing value(s) in column(s): addressline2, state

### Row 609
- Missing value(s) in column(s): addressline2, state

### Row 610
- Missing value(s) in column(s): addressline2, state

### Row 611
- Missing value(s) in column(s): addressline2, state

### Row 612
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 613
- Missing value(s) in column(s): addressline2, state

### Row 614
- Missing value(s) in column(s): addressline2, territory

### Row 615
- Missing value(s) in column(s): addressline2, state

### Row 616
- Missing value(s) in column(s): addressline2, state

### Row 617
- Missing value(s) in column(s): addressline2, state

### Row 618
- Missing value(s) in column(s): addressline2, territory

### Row 619
- Missing value(s) in column(s): addressline2, territory

### Row 621
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 622
- Missing value(s) in column(s): addressline2, state

### Row 623
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 624
- Missing value(s) in column(s): addressline2, state

### Row 625
- Missing value(s) in column(s): addressline2, state

### Row 626
- Missing value(s) in column(s): addressline2, territory

### Row 627
- Missing value(s) in column(s): addressline2, state

### Row 628
- Missing value(s) in column(s): addressline2, state

### Row 630
- Missing value(s) in column(s): addressline2, state

### Row 631
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 632
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 633
- Missing value(s) in column(s): addressline2, territory

### Row 634
- Missing value(s) in column(s): territory

### Row 635
- Missing value(s) in column(s): addressline2, state

### Row 636
- Missing value(s) in column(s): addressline2, territory

### Row 637
- Missing value(s) in column(s): addressline2, postalcode

### Row 638
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 639
- Missing value(s) in column(s): addressline2, state

### Row 640
- Missing value(s) in column(s): addressline2, territory

### Row 641
- Missing value(s) in column(s): addressline2, state

### Row 642
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 643
- Missing value(s) in column(s): addressline2, state

### Row 644
- Missing value(s) in column(s): addressline2, territory

### Row 645
- Missing value(s) in column(s): addressline2, territory

### Row 647
- Missing value(s) in column(s): addressline2, state

### Row 648
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 649
- Missing value(s) in column(s): addressline2, state

### Row 650
- Missing value(s) in column(s): addressline2, territory

### Row 651
- Missing value(s) in column(s): addressline2, state

### Row 652
- Missing value(s) in column(s): addressline2, state

### Row 653
- Missing value(s) in column(s): addressline2, state

### Row 654
- Missing value(s) in column(s): territory

### Row 655
- Missing value(s) in column(s): territory

### Row 656
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 657
- Missing value(s) in column(s): addressline2, state

### Row 658
- Missing value(s) in column(s): addressline2, state

### Row 659
- Missing value(s) in column(s): addressline2, state

### Row 660
- Missing value(s) in column(s): addressline2, state

### Row 661
- Missing value(s) in column(s): addressline2, territory

### Row 662
- Missing value(s) in column(s): addressline2, territory

### Row 663
- Missing value(s) in column(s): addressline2, territory

### Row 664
- Missing value(s) in column(s): addressline2, state

### Row 665
- Missing value(s) in column(s): addressline2, state

### Row 666
- Missing value(s) in column(s): state

### Row 667
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'sales': 9169 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 668
- Missing value(s) in column(s): addressline2, territory

### Row 669
- Missing value(s) in column(s): addressline2, territory

### Row 670
- Missing value(s) in column(s): addressline2, territory

### Row 671
- Missing value(s) in column(s): addressline2, state

### Row 672
- Missing value(s) in column(s): territory

### Row 673
- Missing value(s) in column(s): addressline2, state

### Row 674
- Missing value(s) in column(s): territory

### Row 675
- Missing value(s) in column(s): addressline2, state

### Row 676
- Missing value(s) in column(s): addressline2, territory

### Row 677
- Missing value(s) in column(s): addressline2, territory

### Row 678
- Missing value(s) in column(s): addressline2, state

### Row 679
- Missing value(s) in column(s): addressline2, state

### Row 680
- Missing value(s) in column(s): addressline2, territory

### Row 681
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 682
- Missing value(s) in column(s): addressline2, territory

### Row 683
- Missing value(s) in column(s): addressline2, territory

### Row 684
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 685
- Missing value(s) in column(s): addressline2, state

### Row 686
- Missing value(s) in column(s): addressline2, territory

### Row 687
- Missing value(s) in column(s): addressline2

### Row 688
- Missing value(s) in column(s): territory

### Row 689
- Missing value(s) in column(s): addressline2, state

### Row 690
- Missing value(s) in column(s): addressline2, state

### Row 691
- Missing value(s) in column(s): addressline2, state

### Row 692
- Missing value(s) in column(s): addressline2, state

### Row 693
- Missing value(s) in column(s): state

### Row 694
- Missing value(s) in column(s): addressline2, state

### Row 695
- Missing value(s) in column(s): addressline2, territory

### Row 696
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 697
- Missing value(s) in column(s): addressline2, state

### Row 698
- Missing value(s) in column(s): addressline2, territory

### Row 699
- Missing value(s) in column(s): addressline2, state

### Row 700
- Missing value(s) in column(s): addressline2, territory

### Row 702
- Missing value(s) in column(s): addressline2, state

### Row 703
- Missing value(s) in column(s): addressline2, state

### Row 704
- Missing value(s) in column(s): territory

### Row 705
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 706
- Missing value(s) in column(s): addressline2, state

### Row 707
- Missing value(s) in column(s): addressline2, state

### Row 708
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 709
- Missing value(s) in column(s): addressline2, state

### Row 710
- Missing value(s) in column(s): addressline2, territory

### Row 711
- Missing value(s) in column(s): addressline2, territory

### Row 712
- Missing value(s) in column(s): addressline2, territory

### Row 713
- Missing value(s) in column(s): addressline2, state

### Row 714
- Missing value(s) in column(s): state

### Row 715
- Missing value(s) in column(s): addressline2, territory

### Row 716
- Missing value(s) in column(s): addressline2, territory

### Row 717
- Missing value(s) in column(s): addressline2, territory

### Row 718
- Missing value(s) in column(s): addressline2, territory

### Row 719
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 720
- Missing value(s) in column(s): territory

### Row 721
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 722
- Missing value(s) in column(s): territory

### Row 723
- Missing value(s) in column(s): addressline2, state

### Row 725
- Missing value(s) in column(s): addressline2, state

### Row 726
- Missing value(s) in column(s): addressline2, state

### Row 727
- Missing value(s) in column(s): addressline2, state

### Row 728
- Missing value(s) in column(s): addressline2, state

### Row 729
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 730
- Missing value(s) in column(s): addressline2, territory

### Row 731
- Missing value(s) in column(s): addressline2, territory

### Row 732
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 733
- Missing value(s) in column(s): addressline2, state

### Row 734
- Missing value(s) in column(s): addressline2, territory

### Row 735
- Missing value(s) in column(s): addressline2

### Row 736
- Missing value(s) in column(s): territory

### Row 737
- Missing value(s) in column(s): addressline2, state

### Row 738
- Missing value(s) in column(s): addressline2, state

### Row 739
- Missing value(s) in column(s): addressline2, territory

### Row 740
- Missing value(s) in column(s): addressline2, state

### Row 741
- Missing value(s) in column(s): state

### Row 742
- Missing value(s) in column(s): addressline2, state

### Row 743
- Missing value(s) in column(s): addressline2, territory

### Row 744
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'sales': 1.254e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 745
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 746
- Missing value(s) in column(s): addressline2, state

### Row 747
- Missing value(s) in column(s): addressline2, state

### Row 748
- Missing value(s) in column(s): addressline2, territory

### Row 749
- Missing value(s) in column(s): addressline2, state

### Row 750
- Missing value(s) in column(s): addressline2, territory

### Row 751
- Missing value(s) in column(s): state

### Row 753
- Missing value(s) in column(s): addressline2, state

### Row 754
- Missing value(s) in column(s): addressline2, state

### Row 755
- Missing value(s) in column(s): addressline2, state

### Row 756
- Missing value(s) in column(s): addressline2, territory

### Row 757
- Missing value(s) in column(s): addressline2, state

### Row 758
- Missing value(s) in column(s): addressline2, state

### Row 759
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 760
- Missing value(s) in column(s): addressline2, state

### Row 761
- Missing value(s) in column(s): addressline2, state

### Row 762
- Missing value(s) in column(s): addressline2, territory

### Row 763
- Missing value(s) in column(s): state

### Row 764
- Missing value(s) in column(s): addressline2, territory

### Row 765
- Missing value(s) in column(s): addressline2, state

### Row 766
- Missing value(s) in column(s): state

### Row 767
- Missing value(s) in column(s): addressline2, territory

### Row 768
- Missing value(s) in column(s): addressline2, territory

### Row 769
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 770
- Missing value(s) in column(s): addressline2, territory

### Row 771
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 772
- Missing value(s) in column(s): addressline2, territory

### Row 773
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 775
- Missing value(s) in column(s): addressline2, territory

### Row 777
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 779
- Missing value(s) in column(s): addressline2, state

### Row 780
- Missing value(s) in column(s): addressline2, state

### Row 781
- Missing value(s) in column(s): addressline2, state

### Row 783
- Missing value(s) in column(s): addressline2, state

### Row 784
- Missing value(s) in column(s): addressline2, territory

### Row 785
- Missing value(s) in column(s): addressline2, territory

### Row 786
- Missing value(s) in column(s): addressline2, postalcode

### Row 788
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 789
- Missing value(s) in column(s): addressline2, territory

### Row 790
- Missing value(s) in column(s): addressline2, territory

### Row 791
- Missing value(s) in column(s): addressline2, state

### Row 792
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 793
- Missing value(s) in column(s): state

### Row 794
- Missing value(s) in column(s): addressline2, territory

### Row 795
- Missing value(s) in column(s): addressline2, territory

### Row 796
- Missing value(s) in column(s): addressline2, state

### Row 797
- Missing value(s) in column(s): addressline2, postalcode

### Row 798
- Missing value(s) in column(s): addressline2, territory

### Row 799
- Missing value(s) in column(s): addressline2

### Row 800
- Missing value(s) in column(s): addressline2, state

### Row 801
- Missing value(s) in column(s): addressline2, state

### Row 802
- Missing value(s) in column(s): addressline2, territory

### Row 803
- Missing value(s) in column(s): addressline2, state

### Row 804
- Missing value(s) in column(s): addressline2, territory

### Row 806
- Missing value(s) in column(s): addressline2, state

### Row 807
- Missing value(s) in column(s): addressline2, territory

### Row 808
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 809
- Missing value(s) in column(s): addressline2, territory

### Row 810
- Missing value(s) in column(s): addressline2, state

### Row 811
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 812
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 813
- Missing value(s) in column(s): addressline2, postalcode

### Row 815
- Missing value(s) in column(s): addressline2, territory

### Row 816
- Missing value(s) in column(s): addressline2, territory

### Row 817
- Missing value(s) in column(s): addressline2, territory

### Row 818
- Missing value(s) in column(s): addressline2, state

### Row 819
- Missing value(s) in column(s): addressline2, territory

### Row 820
- Missing value(s) in column(s): addressline2, state

### Row 821
- Missing value(s) in column(s): addressline2, territory

### Row 822
- Missing value(s) in column(s): addressline2, territory

### Row 823
- Missing value(s) in column(s): addressline2, territory

### Row 824
- Missing value(s) in column(s): addressline2, postalcode

### Row 825
- Missing value(s) in column(s): addressline2, territory

### Row 826
- Missing value(s) in column(s): addressline2

### Row 827
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 828
- Missing value(s) in column(s): addressline2, state

### Row 829
- Missing value(s) in column(s): addressline2, state

### Row 830
- Missing value(s) in column(s): addressline2, state

### Row 831
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 834
- Missing value(s) in column(s): addressline2, territory

### Row 835
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 836
- Missing value(s) in column(s): addressline2, state

### Row 837
- Missing value(s) in column(s): addressline2, territory

### Row 838
- Missing value(s) in column(s): addressline2

### Row 839
- Missing value(s) in column(s): addressline2, state

### Row 840
- Missing value(s) in column(s): addressline2, state
- Outlier in 'sales': 9534 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 841
- Missing value(s) in column(s): addressline2, state

### Row 842
- Missing value(s) in column(s): addressline2, state

### Row 843
- Missing value(s) in column(s): addressline2, state

### Row 844
- Missing value(s) in column(s): addressline2, state

### Row 845
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 846
- Missing value(s) in column(s): addressline2, state

### Row 847
- Missing value(s) in column(s): addressline2, territory

### Row 848
- Missing value(s) in column(s): addressline2, territory

### Row 849
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 851
- Missing value(s) in column(s): addressline2, state

### Row 852
- Missing value(s) in column(s): addressline2, territory

### Row 853
- Missing value(s) in column(s): addressline2, state

### Row 854
- Missing value(s) in column(s): addressline2, territory

### Row 855
- Missing value(s) in column(s): addressline2, territory

### Row 856
- Missing value(s) in column(s): addressline2, territory

### Row 857
- Missing value(s) in column(s): addressline2, state

### Row 858
- Missing value(s) in column(s): addressline2, state

### Row 860
- Missing value(s) in column(s): addressline2, state

### Row 861
- Missing value(s) in column(s): addressline2, territory

### Row 862
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 863
- Missing value(s) in column(s): addressline2, territory

### Row 864
- Missing value(s) in column(s): territory

### Row 865
- Missing value(s) in column(s): addressline2, state

### Row 866
- Missing value(s) in column(s): addressline2, territory

### Row 867
- Missing value(s) in column(s): addressline2, state

### Row 868
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 869
- Missing value(s) in column(s): addressline2, state

### Row 870
- Missing value(s) in column(s): addressline2, territory

### Row 871
- Missing value(s) in column(s): addressline2, state

### Row 872
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 873
- Missing value(s) in column(s): addressline2, state

### Row 874
- Missing value(s) in column(s): addressline2, territory

### Row 875
- Missing value(s) in column(s): addressline2, territory

### Row 876
- Missing value(s) in column(s): addressline2, state

### Row 877
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 878
- Missing value(s) in column(s): addressline2, state

### Row 879
- Missing value(s) in column(s): addressline2, territory

### Row 880
- Missing value(s) in column(s): addressline2, state

### Row 881
- Missing value(s) in column(s): addressline2, state

### Row 882
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 883
- Missing value(s) in column(s): addressline2, state

### Row 885
- Missing value(s) in column(s): addressline2, state

### Row 886
- Missing value(s) in column(s): territory

### Row 887
- Missing value(s) in column(s): addressline2

### Row 888
- Missing value(s) in column(s): addressline2, territory

### Row 889
- Missing value(s) in column(s): addressline2

### Row 890
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 891
- Missing value(s) in column(s): addressline2, territory

### Row 892
- Missing value(s) in column(s): addressline2, territory

### Row 893
- Missing value(s) in column(s): addressline2, state

### Row 894
- Missing value(s) in column(s): addressline2, territory

### Row 896
- Missing value(s) in column(s): addressline2, state

### Row 897
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 898
- Missing value(s) in column(s): addressline2, state

### Row 899
- Missing value(s) in column(s): addressline2, territory

### Row 900
- Missing value(s) in column(s): addressline2, territory

### Row 901
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 903
- Missing value(s) in column(s): addressline2, territory

### Row 904
- Missing value(s) in column(s): addressline2, territory

### Row 905
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 907
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 908
- Missing value(s) in column(s): addressline2, state

### Row 909
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 910
- Missing value(s) in column(s): addressline2, state

### Row 912
- Missing value(s) in column(s): addressline2, state

### Row 913
- Missing value(s) in column(s): territory

### Row 914
- Missing value(s) in column(s): addressline2, state

### Row 915
- Missing value(s) in column(s): addressline2, territory

### Row 916
- Missing value(s) in column(s): addressline2

### Row 917
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 918
- Missing value(s) in column(s): addressline2, territory

### Row 919
- Missing value(s) in column(s): addressline2, territory

### Row 920
- Missing value(s) in column(s): addressline2, state

### Row 921
- Missing value(s) in column(s): addressline2, territory

### Row 922
- Missing value(s) in column(s): addressline2, state

### Row 923
- Missing value(s) in column(s): addressline2, state

### Row 924
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 925
- Missing value(s) in column(s): addressline2, state

### Row 926
- Missing value(s) in column(s): addressline2, territory

### Row 927
- Missing value(s) in column(s): addressline2, territory

### Row 928
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 930
- Missing value(s) in column(s): addressline2, territory

### Row 931
- Missing value(s) in column(s): addressline2, territory

### Row 932
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 933
- Missing value(s) in column(s): addressline2, state

### Row 934
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 935
- Missing value(s) in column(s): addressline2, state

### Row 936
- Missing value(s) in column(s): addressline2, state

### Row 937
- Missing value(s) in column(s): addressline2, territory

### Row 938
- Missing value(s) in column(s): addressline2, territory

### Row 939
- Missing value(s) in column(s): addressline2, state

### Row 940
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 941
- Missing value(s) in column(s): addressline2, state

### Row 942
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 943
- Missing value(s) in column(s): addressline2, state

### Row 944
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 945
- Missing value(s) in column(s): addressline2, territory

### Row 946
- Missing value(s) in column(s): addressline2, territory

### Row 947
- Missing value(s) in column(s): addressline2, state

### Row 948
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 949
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 950
- Missing value(s) in column(s): addressline2, state

### Row 951
- Missing value(s) in column(s): addressline2, territory

### Row 952
- Missing value(s) in column(s): addressline2, postalcode

### Row 953
- Missing value(s) in column(s): addressline2, state

### Row 954
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 955
- Missing value(s) in column(s): addressline2, state

### Row 956
- Missing value(s) in column(s): addressline2, state

### Row 957
- Missing value(s) in column(s): addressline2, state

### Row 958
- Missing value(s) in column(s): addressline2, state

### Row 959
- Missing value(s) in column(s): addressline2, territory

### Row 960
- Missing value(s) in column(s): addressline2, territory

### Row 961
- Missing value(s) in column(s): addressline2, state

### Row 962
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 963
- Missing value(s) in column(s): addressline2, state

### Row 965
- Missing value(s) in column(s): addressline2, state

### Row 966
- Missing value(s) in column(s): territory

### Row 967
- Missing value(s) in column(s): addressline2, state

### Row 968
- Missing value(s) in column(s): addressline2, territory

### Row 969
- Missing value(s) in column(s): addressline2

### Row 970
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 971
- Missing value(s) in column(s): addressline2, territory

### Row 972
- Missing value(s) in column(s): addressline2, territory

### Row 973
- Missing value(s) in column(s): addressline2, state

### Row 974
- Missing value(s) in column(s): addressline2, territory

### Row 976
- Missing value(s) in column(s): addressline2, state

### Row 977
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 978
- Missing value(s) in column(s): addressline2, state

### Row 979
- Missing value(s) in column(s): addressline2, territory

### Row 980
- Missing value(s) in column(s): addressline2, territory

### Row 981
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 983
- Missing value(s) in column(s): addressline2, territory

### Row 984
- Missing value(s) in column(s): addressline2, territory

### Row 985
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 986
- Missing value(s) in column(s): addressline2, state

### Row 987
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 988
- Missing value(s) in column(s): addressline2, state

### Row 989
- Missing value(s) in column(s): addressline2, state

### Row 990
- Missing value(s) in column(s): addressline2, state

### Row 991
- Missing value(s) in column(s): addressline2, territory

### Row 992
- Missing value(s) in column(s): addressline2, state

### Row 993
- Missing value(s) in column(s): addressline2, territory

### Row 994
- Missing value(s) in column(s): addressline2, state

### Row 995
- Missing value(s) in column(s): addressline2, territory

### Row 996
- Missing value(s) in column(s): addressline2, territory

### Row 997
- Missing value(s) in column(s): addressline2, state

### Row 998
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 999
- Missing value(s) in column(s): addressline2, postalcode

### Row 1000
- Missing value(s) in column(s): addressline2, territory

### Row 1001
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1002
- Missing value(s) in column(s): addressline2, territory

### Row 1003
- Missing value(s) in column(s): addressline2, state

### Row 1004
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1005
- Missing value(s) in column(s): addressline2, state

### Row 1006
- Missing value(s) in column(s): addressline2, state

### Row 1007
- Missing value(s) in column(s): addressline2, state

### Row 1008
- Missing value(s) in column(s): addressline2, state

### Row 1009
- Missing value(s) in column(s): addressline2, postalcode

### Row 1010
- Missing value(s) in column(s): addressline2, state

### Row 1011
- Missing value(s) in column(s): addressline2, territory

### Row 1012
- Missing value(s) in column(s): addressline2, territory

### Row 1013
- Missing value(s) in column(s): addressline2, state

### Row 1014
- Missing value(s) in column(s): addressline2, territory

### Row 1015
- Missing value(s) in column(s): addressline2, state

### Row 1016
- Missing value(s) in column(s): addressline2, state

### Row 1017
- Missing value(s) in column(s): territory

### Row 1018
- Missing value(s) in column(s): addressline2, state

### Row 1019
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1021
- Missing value(s) in column(s): addressline2, state

### Row 1022
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1023
- Missing value(s) in column(s): addressline2, state

### Row 1024
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1025
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1026
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1027
- Missing value(s) in column(s): addressline2, state

### Row 1028
- Missing value(s) in column(s): addressline2, territory

### Row 1029
- Missing value(s) in column(s): addressline2, territory

### Row 1030
- Missing value(s) in column(s): addressline2, state

### Row 1031
- Missing value(s) in column(s): addressline2, territory

### Row 1032
- Missing value(s) in column(s): addressline2, state

### Row 1033
- Missing value(s) in column(s): addressline2, state

### Row 1034
- Missing value(s) in column(s): addressline2, territory

### Row 1035
- Missing value(s) in column(s): addressline2, state

### Row 1036
- Missing value(s) in column(s): addressline2, state

### Row 1037
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1038
- Missing value(s) in column(s): state

### Row 1039
- Missing value(s) in column(s): addressline2, state

### Row 1040
- Missing value(s) in column(s): addressline2, territory

### Row 1041
- Missing value(s) in column(s): addressline2, territory

### Row 1042
- Missing value(s) in column(s): addressline2, territory

### Row 1043
- Missing value(s) in column(s): addressline2, state

### Row 1044
- Missing value(s) in column(s): addressline2, territory

### Row 1045
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1046
- Missing value(s) in column(s): addressline2, territory

### Row 1047
- Missing value(s) in column(s): addressline2, state

### Row 1048
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1049
- Missing value(s) in column(s): addressline2, territory

### Row 1050
- Missing value(s) in column(s): territory

### Row 1051
- Missing value(s) in column(s): addressline2, territory

### Row 1052
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1054
- Missing value(s) in column(s): territory

### Row 1055
- Missing value(s) in column(s): addressline2, state

### Row 1056
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1058
- Missing value(s) in column(s): addressline2, state

### Row 1059
- Missing value(s) in column(s): addressline2, state

### Row 1060
- Missing value(s) in column(s): addressline2, state

### Row 1061
- Missing value(s) in column(s): addressline2, state

### Row 1062
- Missing value(s) in column(s): addressline2, state
- Outlier in 'sales': 1.189e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 1063
- Missing value(s) in column(s): addressline2, state

### Row 1064
- Missing value(s) in column(s): addressline2, state

### Row 1065
- Missing value(s) in column(s): addressline2, state

### Row 1066
- Missing value(s) in column(s): addressline2, state

### Row 1067
- Missing value(s) in column(s): addressline2, state

### Row 1068
- Missing value(s) in column(s): addressline2, territory

### Row 1069
- Missing value(s) in column(s): addressline2, state

### Row 1070
- Missing value(s) in column(s): addressline2, state

### Row 1071
- Missing value(s) in column(s): addressline2, state

### Row 1072
- Missing value(s) in column(s): addressline2, territory

### Row 1073
- Missing value(s) in column(s): addressline2, territory

### Row 1074
- Missing value(s) in column(s): addressline2, state

### Row 1075
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1076
- Missing value(s) in column(s): addressline2, postalcode

### Row 1077
- Missing value(s) in column(s): addressline2, territory

### Row 1078
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1079
- Missing value(s) in column(s): addressline2, territory

### Row 1080
- Missing value(s) in column(s): addressline2, state

### Row 1081
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1082
- Missing value(s) in column(s): addressline2, state

### Row 1083
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1084
- Missing value(s) in column(s): addressline2, state

### Row 1085
- Missing value(s) in column(s): addressline2, state

### Row 1086
- Missing value(s) in column(s): addressline2, postalcode

### Row 1087
- Missing value(s) in column(s): addressline2, state

### Row 1088
- Missing value(s) in column(s): addressline2, territory

### Row 1089
- Missing value(s) in column(s): addressline2, territory

### Row 1090
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1091
- Missing value(s) in column(s): addressline2, state

### Row 1092
- Missing value(s) in column(s): addressline2, territory

### Row 1093
- Missing value(s) in column(s): addressline2, territory

### Row 1094
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1096
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1097
- Missing value(s) in column(s): addressline2, state

### Row 1098
- Missing value(s) in column(s): addressline2, state

### Row 1099
- Missing value(s) in column(s): addressline2, state

### Row 1100
- Missing value(s) in column(s): addressline2, state

### Row 1101
- Missing value(s) in column(s): addressline2, state

### Row 1102
- Missing value(s) in column(s): addressline2, state

### Row 1103
- Missing value(s) in column(s): addressline2

### Row 1104
- Missing value(s) in column(s): addressline2, territory

### Row 1105
- Missing value(s) in column(s): addressline2, state

### Row 1106
- Missing value(s) in column(s): addressline2, state

### Row 1107
- Missing value(s) in column(s): addressline2, state

### Row 1108
- Missing value(s) in column(s): territory

### Row 1109
- Missing value(s) in column(s): addressline2, territory

### Row 1111
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1112
- Missing value(s) in column(s): addressline2, state

### Row 1113
- Missing value(s) in column(s): addressline2, territory

### Row 1114
- Missing value(s) in column(s): addressline2, state

### Row 1115
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1116
- Missing value(s) in column(s): addressline2, state

### Row 1118
- Missing value(s) in column(s): addressline2, territory

### Row 1119
- Missing value(s) in column(s): territory

### Row 1120
- Missing value(s) in column(s): addressline2, state

### Row 1121
- Missing value(s) in column(s): addressline2, territory

### Row 1122
- Missing value(s) in column(s): addressline2

### Row 1123
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1124
- Missing value(s) in column(s): addressline2, territory

### Row 1125
- Missing value(s) in column(s): addressline2, state

### Row 1126
- Missing value(s) in column(s): addressline2, state

### Row 1127
- Missing value(s) in column(s): addressline2, territory

### Row 1128
- Missing value(s) in column(s): addressline2, state

### Row 1129
- Missing value(s) in column(s): addressline2, territory

### Row 1130
- Missing value(s) in column(s): addressline2, state

### Row 1131
- Missing value(s) in column(s): addressline2, territory

### Row 1132
- Missing value(s) in column(s): addressline2, state

### Row 1133
- Missing value(s) in column(s): addressline2, postalcode, territory
- Outlier in 'sales': 1.134e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 1135
- Missing value(s) in column(s): addressline2, territory

### Row 1136
- Missing value(s) in column(s): addressline2, territory

### Row 1137
- Missing value(s) in column(s): addressline2, territory

### Row 1138
- Missing value(s) in column(s): addressline2, state

### Row 1139
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1140
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1141
- Missing value(s) in column(s): addressline2, state

### Row 1142
- Missing value(s) in column(s): addressline2, territory

### Row 1143
- Missing value(s) in column(s): addressline2, territory

### Row 1144
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1146
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1147
- Missing value(s) in column(s): addressline2, state

### Row 1148
- Missing value(s) in column(s): addressline2, state

### Row 1149
- Missing value(s) in column(s): addressline2, state

### Row 1150
- Missing value(s) in column(s): addressline2, state

### Row 1151
- Missing value(s) in column(s): addressline2, state

### Row 1152
- Missing value(s) in column(s): addressline2, state

### Row 1153
- Missing value(s) in column(s): addressline2

### Row 1154
- Missing value(s) in column(s): addressline2, territory

### Row 1155
- Missing value(s) in column(s): addressline2, state

### Row 1156
- Missing value(s) in column(s): addressline2, state

### Row 1157
- Missing value(s) in column(s): addressline2, state

### Row 1158
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1159
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1161
- Missing value(s) in column(s): addressline2, state

### Row 1162
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1163
- Missing value(s) in column(s): addressline2, state

### Row 1164
- Missing value(s) in column(s): addressline2, territory

### Row 1165
- Missing value(s) in column(s): addressline2, territory

### Row 1166
- Missing value(s) in column(s): addressline2, state

### Row 1167
- Missing value(s) in column(s): addressline2, state

### Row 1169
- Missing value(s) in column(s): addressline2, state

### Row 1170
- Missing value(s) in column(s): addressline2, territory

### Row 1171
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1172
- Missing value(s) in column(s): addressline2, territory

### Row 1173
- Missing value(s) in column(s): territory

### Row 1174
- Missing value(s) in column(s): addressline2, state

### Row 1175
- Missing value(s) in column(s): addressline2, territory

### Row 1176
- Missing value(s) in column(s): addressline2, postalcode

### Row 1177
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1178
- Missing value(s) in column(s): addressline2, state

### Row 1179
- Missing value(s) in column(s): addressline2, territory

### Row 1180
- Missing value(s) in column(s): addressline2, state

### Row 1181
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1182
- Missing value(s) in column(s): addressline2, state

### Row 1183
- Missing value(s) in column(s): addressline2, territory

### Row 1184
- Missing value(s) in column(s): addressline2, territory

### Row 1185
- Missing value(s) in column(s): addressline2, state

### Row 1186
- Missing value(s) in column(s): addressline2, territory

### Row 1187
- Missing value(s) in column(s): addressline2, state

### Row 1188
- Missing value(s) in column(s): addressline2, state
- Outlier in 'quantityordered': 65 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])
- Outlier in 'sales': 1.047e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 1189
- Missing value(s) in column(s): addressline2, state

### Row 1190
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1191
- Missing value(s) in column(s): addressline2, state

### Row 1192
- Missing value(s) in column(s): addressline2, territory

### Row 1193
- Missing value(s) in column(s): addressline2, territory

### Row 1194
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1196
- Missing value(s) in column(s): addressline2, state

### Row 1197
- Missing value(s) in column(s): addressline2, state

### Row 1198
- Missing value(s) in column(s): addressline2, state

### Row 1199
- Missing value(s) in column(s): addressline2, state

### Row 1200
- Missing value(s) in column(s): territory

### Row 1201
- Missing value(s) in column(s): addressline2, state

### Row 1202
- Missing value(s) in column(s): addressline2, territory

### Row 1203
- Missing value(s) in column(s): addressline2, territory

### Row 1204
- Missing value(s) in column(s): addressline2, state

### Row 1205
- Missing value(s) in column(s): addressline2, state

### Row 1206
- Missing value(s) in column(s): addressline2, state

### Row 1207
- Missing value(s) in column(s): territory

### Row 1208
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1210
- Missing value(s) in column(s): addressline2, state

### Row 1211
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1212
- Missing value(s) in column(s): addressline2, state

### Row 1213
- Missing value(s) in column(s): addressline2, territory

### Row 1214
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1215
- Missing value(s) in column(s): addressline2, state

### Row 1216
- Missing value(s) in column(s): addressline2, state

### Row 1217
- Missing value(s) in column(s): addressline2, territory

### Row 1218
- Missing value(s) in column(s): addressline2, territory

### Row 1219
- Missing value(s) in column(s): addressline2, state

### Row 1220
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1221
- Missing value(s) in column(s): addressline2, state

### Row 1222
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1223
- Missing value(s) in column(s): addressline2, state

### Row 1224
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1225
- Missing value(s) in column(s): addressline2, territory

### Row 1226
- Missing value(s) in column(s): addressline2, territory

### Row 1227
- Missing value(s) in column(s): addressline2, state

### Row 1228
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1229
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1230
- Missing value(s) in column(s): addressline2, state

### Row 1231
- Missing value(s) in column(s): addressline2, territory

### Row 1232
- Missing value(s) in column(s): addressline2, postalcode

### Row 1233
- Missing value(s) in column(s): addressline2, state

### Row 1234
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1235
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1236
- Missing value(s) in column(s): addressline2, state

### Row 1237
- Missing value(s) in column(s): addressline2, state

### Row 1238
- Missing value(s) in column(s): addressline2, state

### Row 1239
- Missing value(s) in column(s): addressline2, territory

### Row 1240
- Missing value(s) in column(s): addressline2

### Row 1241
- Missing value(s) in column(s): addressline2, state

### Row 1242
- Missing value(s) in column(s): addressline2, state

### Row 1243
- Missing value(s) in column(s): territory

### Row 1244
- Missing value(s) in column(s): addressline2, territory

### Row 1245
- Missing value(s) in column(s): addressline2

### Row 1246
- Missing value(s) in column(s): addressline2, state

### Row 1247
- Missing value(s) in column(s): addressline2, state

### Row 1248
- Missing value(s) in column(s): addressline2, territory

### Row 1249
- Missing value(s) in column(s): addressline2, territory

### Row 1250
- Missing value(s) in column(s): addressline2, territory

### Row 1251
- Missing value(s) in column(s): state

### Row 1252
- Missing value(s) in column(s): addressline2, state

### Row 1253
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1254
- Missing value(s) in column(s): addressline2, territory

### Row 1255
- Missing value(s) in column(s): addressline2, territory

### Row 1256
- Missing value(s) in column(s): addressline2, territory

### Row 1257
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1258
- Missing value(s) in column(s): addressline2, state

### Row 1259
- Missing value(s) in column(s): territory

### Row 1260
- Missing value(s) in column(s): territory

### Row 1261
- Missing value(s) in column(s): territory

### Row 1262
- Missing value(s) in column(s): addressline2, state

### Row 1263
- Missing value(s) in column(s): addressline2, postalcode

### Row 1264
- Missing value(s) in column(s): addressline2, state

### Row 1265
- Missing value(s) in column(s): addressline2, state

### Row 1266
- Missing value(s) in column(s): addressline2, territory

### Row 1267
- Missing value(s) in column(s): addressline2, territory

### Row 1268
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1269
- Missing value(s) in column(s): addressline2, territory

### Row 1271
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1272
- Missing value(s) in column(s): addressline2, state

### Row 1273
- Missing value(s) in column(s): addressline2, territory

### Row 1274
- Missing value(s) in column(s): addressline2

### Row 1275
- Missing value(s) in column(s): territory

### Row 1276
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1277
- Missing value(s) in column(s): addressline2, state

### Row 1278
- Missing value(s) in column(s): addressline2, state

### Row 1279
- Missing value(s) in column(s): addressline2, state

### Row 1280
- Missing value(s) in column(s): state

### Row 1281
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1282
- Missing value(s) in column(s): addressline2, state

### Row 1283
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1284
- Missing value(s) in column(s): addressline2, state

### Row 1285
- Missing value(s) in column(s): addressline2, territory

### Row 1286
- Missing value(s) in column(s): addressline2, state

### Row 1287
- Missing value(s) in column(s): addressline2, territory

### Row 1288
- Outlier in 'quantityordered': 66 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])

### Row 1289
- Missing value(s) in column(s): addressline2, state

### Row 1290
- Missing value(s) in column(s): addressline2, state

### Row 1291
- Missing value(s) in column(s): addressline2, state

### Row 1292
- Missing value(s) in column(s): addressline2, territory

### Row 1293
- Missing value(s) in column(s): addressline2, state

### Row 1294
- Missing value(s) in column(s): addressline2, territory

### Row 1295
- Missing value(s) in column(s): addressline2, state

### Row 1296
- Missing value(s) in column(s): addressline2, territory

### Row 1297
- Missing value(s) in column(s): addressline2, state

### Row 1298
- Missing value(s) in column(s): addressline2, state

### Row 1299
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1300
- Missing value(s) in column(s): addressline2, postalcode

### Row 1301
- Missing value(s) in column(s): addressline2, territory

### Row 1302
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1303
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1304
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1305
- Missing value(s) in column(s): addressline2, state

### Row 1306
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1307
- Missing value(s) in column(s): addressline2, state

### Row 1308
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1309
- Missing value(s) in column(s): territory

### Row 1310
- Missing value(s) in column(s): addressline2, state

### Row 1311
- Missing value(s) in column(s): addressline2, postalcode

### Row 1312
- Missing value(s) in column(s): addressline2, state

### Row 1313
- Missing value(s) in column(s): addressline2, territory

### Row 1314
- Missing value(s) in column(s): addressline2, territory

### Row 1315
- Missing value(s) in column(s): addressline2, state

### Row 1316
- Missing value(s) in column(s): addressline2, state

### Row 1317
- Missing value(s) in column(s): addressline2, state

### Row 1318
- Missing value(s) in column(s): addressline2, territory

### Row 1319
- Missing value(s) in column(s): addressline2, state

### Row 1320
- Missing value(s) in column(s): addressline2, state

### Row 1321
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1322
- Missing value(s) in column(s): addressline2, territory

### Row 1323
- Missing value(s) in column(s): addressline2, state

### Row 1324
- Missing value(s) in column(s): addressline2, territory

### Row 1325
- Missing value(s) in column(s): state

### Row 1326
- Missing value(s) in column(s): addressline2, territory

### Row 1327
- Missing value(s) in column(s): addressline2, territory

### Row 1328
- Missing value(s) in column(s): state

### Row 1330
- Missing value(s) in column(s): addressline2, territory

### Row 1331
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1332
- Missing value(s) in column(s): addressline2, territory

### Row 1333
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1334
- Missing value(s) in column(s): addressline2, state

### Row 1335
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1337
- Missing value(s) in column(s): addressline2, territory

### Row 1339
- Missing value(s) in column(s): addressline2, territory

### Row 1340
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1341
- Missing value(s) in column(s): addressline2, state

### Row 1342
- Missing value(s) in column(s): addressline2, state

### Row 1343
- Missing value(s) in column(s): addressline2, territory

### Row 1344
- Missing value(s) in column(s): addressline2, state

### Row 1345
- Missing value(s) in column(s): addressline2, territory

### Row 1346
- Missing value(s) in column(s): addressline2, state

### Row 1347
- Missing value(s) in column(s): addressline2, state

### Row 1348
- Missing value(s) in column(s): addressline2

### Row 1349
- Missing value(s) in column(s): addressline2, territory

### Row 1350
- Missing value(s) in column(s): addressline2, state

### Row 1351
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1352
- Missing value(s) in column(s): addressline2, territory

### Row 1353
- Missing value(s) in column(s): addressline2, territory

### Row 1354
- Missing value(s) in column(s): addressline2, territory

### Row 1355
- Missing value(s) in column(s): addressline2, postalcode

### Row 1357
- Missing value(s) in column(s): addressline2, territory

### Row 1358
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1359
- Missing value(s) in column(s): addressline2, state

### Row 1360
- Missing value(s) in column(s): addressline2, territory

### Row 1361
- Missing value(s) in column(s): territory

### Row 1362
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1363
- Missing value(s) in column(s): addressline2, state

### Row 1364
- Missing value(s) in column(s): addressline2, state

### Row 1366
- Missing value(s) in column(s): addressline2, territory

### Row 1367
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1368
- Missing value(s) in column(s): addressline2, state

### Row 1369
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1370
- Missing value(s) in column(s): addressline2, state

### Row 1371
- Missing value(s) in column(s): addressline2, territory

### Row 1372
- Missing value(s) in column(s): addressline2, territory

### Row 1373
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1375
- Missing value(s) in column(s): addressline2, state

### Row 1376
- Missing value(s) in column(s): addressline2, state

### Row 1377
- Missing value(s) in column(s): addressline2, state

### Row 1378
- Missing value(s) in column(s): addressline2, state

### Row 1379
- Missing value(s) in column(s): addressline2, state

### Row 1380
- Missing value(s) in column(s): addressline2, state

### Row 1381
- Missing value(s) in column(s): addressline2, territory

### Row 1382
- Missing value(s) in column(s): addressline2, territory

### Row 1383
- Missing value(s) in column(s): addressline2, state

### Row 1384
- Missing value(s) in column(s): addressline2, state

### Row 1385
- Missing value(s) in column(s): addressline2, state

### Row 1386
- Missing value(s) in column(s): territory

### Row 1387
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1389
- Missing value(s) in column(s): addressline2, state

### Row 1390
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1391
- Missing value(s) in column(s): addressline2, state

### Row 1392
- Missing value(s) in column(s): addressline2, territory

### Row 1393
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1394
- Missing value(s) in column(s): addressline2, territory

### Row 1396
- Missing value(s) in column(s): addressline2, state

### Row 1397
- Missing value(s) in column(s): addressline2, state

### Row 1398
- Missing value(s) in column(s): addressline2, territory

### Row 1399
- Missing value(s) in column(s): addressline2

### Row 1400
- Missing value(s) in column(s): territory

### Row 1401
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1402
- Missing value(s) in column(s): addressline2, state

### Row 1403
- Missing value(s) in column(s): addressline2, state

### Row 1404
- Missing value(s) in column(s): territory

### Row 1405
- Missing value(s) in column(s): addressline2, state

### Row 1406
- Missing value(s) in column(s): state

### Row 1407
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1408
- Missing value(s) in column(s): addressline2, state

### Row 1409
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1410
- Missing value(s) in column(s): addressline2, state

### Row 1411
- Missing value(s) in column(s): addressline2, territory

### Row 1412
- Missing value(s) in column(s): addressline2, state

### Row 1413
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'quantityordered': 66 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])

### Row 1415
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1416
- Missing value(s) in column(s): addressline2, territory

### Row 1418
- Missing value(s) in column(s): addressline2, state

### Row 1419
- Missing value(s) in column(s): addressline2, territory

### Row 1420
- Missing value(s) in column(s): addressline2, territory

### Row 1421
- Missing value(s) in column(s): addressline2, territory

### Row 1422
- Missing value(s) in column(s): territory

### Row 1423
- Missing value(s) in column(s): addressline2, state

### Row 1424
- Missing value(s) in column(s): addressline2, territory

### Row 1425
- Missing value(s) in column(s): addressline2, state

### Row 1426
- Missing value(s) in column(s): territory

### Row 1427
- Missing value(s) in column(s): addressline2, state

### Row 1428
- Missing value(s) in column(s): state

### Row 1429
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1430
- Missing value(s) in column(s): addressline2, state

### Row 1431
- Missing value(s) in column(s): addressline2, territory

### Row 1432
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1433
- Missing value(s) in column(s): addressline2, state

### Row 1434
- Missing value(s) in column(s): addressline2, territory

### Row 1435
- Missing value(s) in column(s): addressline2, state

### Row 1436
- Missing value(s) in column(s): addressline2, territory

### Row 1438
- Missing value(s) in column(s): addressline2, state

### Row 1439
- Missing value(s) in column(s): territory

### Row 1440
- Missing value(s) in column(s): territory

### Row 1441
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1442
- Missing value(s) in column(s): addressline2

### Row 1443
- Missing value(s) in column(s): addressline2, state

### Row 1444
- Missing value(s) in column(s): addressline2, state

### Row 1445
- Missing value(s) in column(s): addressline2, state

### Row 1446
- Missing value(s) in column(s): addressline2, territory

### Row 1447
- Missing value(s) in column(s): addressline2, territory

### Row 1448
- Missing value(s) in column(s): state

### Row 1449
- Missing value(s) in column(s): addressline2, state

### Row 1450
- Missing value(s) in column(s): addressline2, state

### Row 1451
- Missing value(s) in column(s): state

### Row 1452
- Missing value(s) in column(s): addressline2, territory

### Row 1453
- Missing value(s) in column(s): addressline2, territory

### Row 1454
- Missing value(s) in column(s): addressline2, territory

### Row 1455
- Missing value(s) in column(s): addressline2, territory

### Row 1456
- Missing value(s) in column(s): addressline2, state

### Row 1457
- Missing value(s) in column(s): territory

### Row 1458
- Missing value(s) in column(s): addressline2, state

### Row 1459
- Missing value(s) in column(s): territory

### Row 1460
- Missing value(s) in column(s): addressline2, state

### Row 1461
- Missing value(s) in column(s): addressline2, territory

### Row 1462
- Missing value(s) in column(s): addressline2, state

### Row 1463
- Missing value(s) in column(s): addressline2, state

### Row 1464
- Missing value(s) in column(s): addressline2, state

### Row 1465
- Missing value(s) in column(s): addressline2, state

### Row 1466
- Missing value(s) in column(s): addressline2, territory

### Row 1468
- Missing value(s) in column(s): addressline2, state

### Row 1469
- Missing value(s) in column(s): addressline2, territory

### Row 1470
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1471
- Missing value(s) in column(s): addressline2, territory

### Row 1472
- Missing value(s) in column(s): addressline2, state

### Row 1473
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1474
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1475
- Missing value(s) in column(s): addressline2, state

### Row 1477
- Missing value(s) in column(s): territory

### Row 1478
- Missing value(s) in column(s): addressline2, territory

### Row 1479
- Missing value(s) in column(s): addressline2, territory

### Row 1480
- Missing value(s) in column(s): addressline2, state

### Row 1481
- Missing value(s) in column(s): addressline2, territory

### Row 1482
- Missing value(s) in column(s): addressline2, state

### Row 1483
- Missing value(s) in column(s): addressline2, state

### Row 1484
- Missing value(s) in column(s): addressline2, territory

### Row 1485
- Missing value(s) in column(s): addressline2, territory

### Row 1486
- Missing value(s) in column(s): addressline2, postalcode

### Row 1487
- Missing value(s) in column(s): addressline2, territory

### Row 1488
- Missing value(s) in column(s): addressline2

### Row 1489
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1490
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1491
- Missing value(s) in column(s): addressline2, state

### Row 1492
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1493
- Missing value(s) in column(s): addressline2, state

### Row 1494
- Missing value(s) in column(s): addressline2, state

### Row 1496
- Missing value(s) in column(s): addressline2, state

### Row 1497
- Missing value(s) in column(s): addressline2, territory

### Row 1498
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1499
- Missing value(s) in column(s): addressline2, territory

### Row 1500
- Missing value(s) in column(s): territory

### Row 1501
- Missing value(s) in column(s): addressline2, state

### Row 1502
- Missing value(s) in column(s): addressline2, territory

### Row 1503
- Missing value(s) in column(s): addressline2, state

### Row 1504
- Missing value(s) in column(s): addressline2, state

### Row 1505
- Missing value(s) in column(s): addressline2, territory

### Row 1506
- Missing value(s) in column(s): state

### Row 1507
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1508
- Missing value(s) in column(s): addressline2, state

### Row 1509
- Missing value(s) in column(s): addressline2, territory

### Row 1510
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1511
- Missing value(s) in column(s): addressline2, state

### Row 1512
- Missing value(s) in column(s): addressline2, territory

### Row 1513
- Missing value(s) in column(s): addressline2, state

### Row 1514
- Missing value(s) in column(s): addressline2, territory

### Row 1516
- Missing value(s) in column(s): addressline2, state

### Row 1518
- Missing value(s) in column(s): addressline2, state

### Row 1519
- Missing value(s) in column(s): addressline2, territory

### Row 1520
- Missing value(s) in column(s): addressline2, territory

### Row 1521
- Missing value(s) in column(s): addressline2, postalcode

### Row 1523
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1524
- Missing value(s) in column(s): addressline2, territory

### Row 1525
- Missing value(s) in column(s): addressline2, state

### Row 1526
- Missing value(s) in column(s): addressline2, state

### Row 1527
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1528
- Missing value(s) in column(s): state

### Row 1529
- Missing value(s) in column(s): addressline2, territory

### Row 1530
- Missing value(s) in column(s): addressline2, postalcode

### Row 1531
- Missing value(s) in column(s): addressline2, state

### Row 1532
- Missing value(s) in column(s): addressline2, postalcode

### Row 1533
- Missing value(s) in column(s): addressline2, territory

### Row 1534
- Missing value(s) in column(s): addressline2

### Row 1535
- Missing value(s) in column(s): addressline2, state

### Row 1536
- Missing value(s) in column(s): addressline2, state

### Row 1537
- Missing value(s) in column(s): addressline2, territory

### Row 1538
- Missing value(s) in column(s): addressline2, state

### Row 1539
- Missing value(s) in column(s): addressline2, state

### Row 1540
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1541
- Missing value(s) in column(s): addressline2, territory

### Row 1542
- Missing value(s) in column(s): addressline2, territory

### Row 1543
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1544
- Missing value(s) in column(s): addressline2, state

### Row 1545
- Missing value(s) in column(s): addressline2, territory

### Row 1546
- Missing value(s) in column(s): addressline2

### Row 1547
- Missing value(s) in column(s): addressline2, state

### Row 1548
- Missing value(s) in column(s): addressline2, state

### Row 1549
- Missing value(s) in column(s): addressline2, state

### Row 1550
- Missing value(s) in column(s): addressline2, territory

### Row 1551
- Missing value(s) in column(s): addressline2, state

### Row 1552
- Missing value(s) in column(s): state

### Row 1553
- Missing value(s) in column(s): addressline2, state

### Row 1554
- Missing value(s) in column(s): addressline2, territory

### Row 1555
- Missing value(s) in column(s): addressline2, territory

### Row 1556
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1557
- Missing value(s) in column(s): addressline2, state

### Row 1558
- Missing value(s) in column(s): addressline2, state
- Outlier in 'sales': 9720 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 1559
- Missing value(s) in column(s): addressline2, territory

### Row 1560
- Missing value(s) in column(s): addressline2, state

### Row 1562
- Missing value(s) in column(s): state

### Row 1564
- Missing value(s) in column(s): addressline2, territory

### Row 1566
- Missing value(s) in column(s): addressline2, state

### Row 1567
- Missing value(s) in column(s): addressline2, territory

### Row 1568
- Missing value(s) in column(s): addressline2, state

### Row 1569
- Missing value(s) in column(s): addressline2, territory

### Row 1570
- Missing value(s) in column(s): addressline2, state

### Row 1571
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1572
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1573
- Missing value(s) in column(s): addressline2, postalcode

### Row 1575
- Missing value(s) in column(s): addressline2, territory

### Row 1576
- Missing value(s) in column(s): addressline2, territory

### Row 1577
- Missing value(s) in column(s): addressline2, territory

### Row 1578
- Missing value(s) in column(s): addressline2, state

### Row 1579
- Missing value(s) in column(s): addressline2, territory

### Row 1580
- Missing value(s) in column(s): state

### Row 1581
- Missing value(s) in column(s): addressline2, territory

### Row 1582
- Missing value(s) in column(s): addressline2, territory

### Row 1583
- Missing value(s) in column(s): addressline2, territory

### Row 1584
- Missing value(s) in column(s): addressline2, state

### Row 1585
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1586
- Missing value(s) in column(s): addressline2, state

### Row 1587
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1588
- Missing value(s) in column(s): addressline2, state

### Row 1589
- Missing value(s) in column(s): addressline2, state

### Row 1590
- Missing value(s) in column(s): addressline2, state

### Row 1591
- Missing value(s) in column(s): addressline2, state

### Row 1592
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1593
- Missing value(s) in column(s): addressline2, territory

### Row 1594
- Missing value(s) in column(s): addressline2, state

### Row 1595
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1596
- Missing value(s) in column(s): addressline2, state

### Row 1597
- Missing value(s) in column(s): addressline2, territory

### Row 1598
- Missing value(s) in column(s): addressline2, state

### Row 1599
- Missing value(s) in column(s): addressline2, state

### Row 1600
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1601
- Missing value(s) in column(s): addressline2, postalcode

### Row 1602
- Missing value(s) in column(s): addressline2, territory

### Row 1603
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1604
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1605
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1606
- Missing value(s) in column(s): addressline2, state

### Row 1607
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1608
- Missing value(s) in column(s): addressline2, state

### Row 1609
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1610
- Missing value(s) in column(s): territory

### Row 1611
- Missing value(s) in column(s): addressline2, state

### Row 1612
- Missing value(s) in column(s): addressline2, postalcode

### Row 1613
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1614
- Missing value(s) in column(s): addressline2, territory

### Row 1615
- Missing value(s) in column(s): addressline2, territory

### Row 1616
- Missing value(s) in column(s): addressline2, state

### Row 1617
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1618
- Missing value(s) in column(s): addressline2, territory

### Row 1619
- Missing value(s) in column(s): addressline2, territory

### Row 1620
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1621
- Missing value(s) in column(s): addressline2, state

### Row 1622
- Missing value(s) in column(s): addressline2, territory

### Row 1623
- Missing value(s) in column(s): addressline2

### Row 1624
- Missing value(s) in column(s): addressline2, state

### Row 1625
- Missing value(s) in column(s): addressline2, state

### Row 1626
- Missing value(s) in column(s): addressline2, state

### Row 1627
- Missing value(s) in column(s): addressline2, state

### Row 1628
- Missing value(s) in column(s): addressline2, state

### Row 1629
- Missing value(s) in column(s): addressline2, state

### Row 1630
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1631
- Missing value(s) in column(s): addressline2, state

### Row 1632
- Missing value(s) in column(s): addressline2, territory

### Row 1633
- Missing value(s) in column(s): addressline2, territory

### Row 1634
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1635
- Missing value(s) in column(s): addressline2, state

### Row 1636
- Missing value(s) in column(s): addressline2, state

### Row 1637
- Missing value(s) in column(s): addressline2, territory

### Row 1638
- Missing value(s) in column(s): addressline2, state

### Row 1640
- Missing value(s) in column(s): addressline2, territory

### Row 1641
- Missing value(s) in column(s): addressline2, state

### Row 1642
- Missing value(s) in column(s): addressline2, state

### Row 1643
- Missing value(s) in column(s): addressline2, state

### Row 1644
- Missing value(s) in column(s): addressline2, territory

### Row 1645
- Missing value(s) in column(s): addressline2, state

### Row 1646
- Missing value(s) in column(s): addressline2, state

### Row 1647
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1648
- Missing value(s) in column(s): addressline2, state

### Row 1649
- Missing value(s) in column(s): addressline2, state

### Row 1650
- Missing value(s) in column(s): addressline2, territory

### Row 1651
- Missing value(s) in column(s): state

### Row 1652
- Missing value(s) in column(s): addressline2, territory

### Row 1653
- Missing value(s) in column(s): addressline2, state

### Row 1654
- Missing value(s) in column(s): state

### Row 1655
- Missing value(s) in column(s): addressline2, territory

### Row 1656
- Missing value(s) in column(s): addressline2, territory

### Row 1657
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1658
- Missing value(s) in column(s): addressline2, territory

### Row 1659
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1660
- Missing value(s) in column(s): territory

### Row 1661
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1662
- Missing value(s) in column(s): addressline2, state

### Row 1663
- Missing value(s) in column(s): addressline2, state

### Row 1664
- Missing value(s) in column(s): addressline2, territory

### Row 1665
- Missing value(s) in column(s): addressline2, territory

### Row 1666
- Missing value(s) in column(s): addressline2, state
- Outlier in 'quantityordered': 70 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])

### Row 1667
- Missing value(s) in column(s): addressline2, state

### Row 1668
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1669
- Missing value(s) in column(s): addressline2, state

### Row 1670
- Missing value(s) in column(s): addressline2, territory

### Row 1671
- Missing value(s) in column(s): addressline2, territory

### Row 1672
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1674
- Missing value(s) in column(s): addressline2, state

### Row 1675
- Missing value(s) in column(s): addressline2, state

### Row 1676
- Missing value(s) in column(s): addressline2, state

### Row 1677
- Missing value(s) in column(s): addressline2, state

### Row 1678
- Missing value(s) in column(s): territory

### Row 1679
- Missing value(s) in column(s): addressline2, state

### Row 1680
- Missing value(s) in column(s): addressline2, territory

### Row 1681
- Missing value(s) in column(s): addressline2, territory

### Row 1682
- Missing value(s) in column(s): addressline2, territory

### Row 1683
- Missing value(s) in column(s): addressline2, state

### Row 1684
- Missing value(s) in column(s): addressline2, state

### Row 1685
- Missing value(s) in column(s): territory

### Row 1686
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1687
- Missing value(s) in column(s): addressline2, state

### Row 1688
- Missing value(s) in column(s): addressline2, state

### Row 1689
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1690
- Missing value(s) in column(s): addressline2, state

### Row 1691
- Missing value(s) in column(s): addressline2, territory

### Row 1692
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1693
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1694
- Missing value(s) in column(s): addressline2, territory

### Row 1696
- Missing value(s) in column(s): addressline2, state

### Row 1697
- Missing value(s) in column(s): addressline2, territory

### Row 1698
- Missing value(s) in column(s): addressline2, territory

### Row 1699
- Missing value(s) in column(s): addressline2, territory

### Row 1700
- Missing value(s) in column(s): territory

### Row 1701
- Missing value(s) in column(s): addressline2, state

### Row 1702
- Missing value(s) in column(s): addressline2, state

### Row 1703
- Missing value(s) in column(s): addressline2, state

### Row 1704
- Missing value(s) in column(s): territory

### Row 1705
- Missing value(s) in column(s): addressline2, state

### Row 1706
- Missing value(s) in column(s): state

### Row 1707
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1708
- Missing value(s) in column(s): addressline2, state

### Row 1709
- Missing value(s) in column(s): addressline2, territory

### Row 1710
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1711
- Missing value(s) in column(s): addressline2, territory

### Row 1712
- Missing value(s) in column(s): addressline2, territory

### Row 1713
- Missing value(s) in column(s): addressline2, state

### Row 1714
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'quantityordered': 76 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])

### Row 1716
- Missing value(s) in column(s): addressline2, state

### Row 1717
- Missing value(s) in column(s): addressline2, state

### Row 1718
- Missing value(s) in column(s): territory

### Row 1719
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1720
- Missing value(s) in column(s): addressline2, state

### Row 1721
- Missing value(s) in column(s): addressline2, state

### Row 1722
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1723
- Missing value(s) in column(s): addressline2, state

### Row 1724
- Missing value(s) in column(s): addressline2, territory

### Row 1725
- Missing value(s) in column(s): addressline2, territory

### Row 1726
- Missing value(s) in column(s): addressline2, territory

### Row 1727
- Missing value(s) in column(s): addressline2, territory

### Row 1728
- Missing value(s) in column(s): addressline2, state

### Row 1729
- Missing value(s) in column(s): state

### Row 1730
- Missing value(s) in column(s): addressline2, territory

### Row 1731
- Missing value(s) in column(s): addressline2, territory

### Row 1732
- Missing value(s) in column(s): addressline2, territory

### Row 1733
- Missing value(s) in column(s): addressline2, territory

### Row 1734
- Missing value(s) in column(s): addressline2, state

### Row 1735
- Missing value(s) in column(s): territory

### Row 1736
- Missing value(s) in column(s): addressline2, territory

### Row 1737
- Missing value(s) in column(s): territory

### Row 1738
- Missing value(s) in column(s): addressline2, state

### Row 1739
- Missing value(s) in column(s): addressline2, territory

### Row 1740
- Missing value(s) in column(s): addressline2, state

### Row 1741
- Missing value(s) in column(s): addressline2, state

### Row 1742
- Missing value(s) in column(s): addressline2, state

### Row 1743
- Missing value(s) in column(s): addressline2, state

### Row 1744
- Missing value(s) in column(s): addressline2, state

### Row 1745
- Missing value(s) in column(s): addressline2, state

### Row 1746
- Missing value(s) in column(s): addressline2, territory

### Row 1747
- Missing value(s) in column(s): addressline2, territory

### Row 1748
- Missing value(s) in column(s): addressline2, state

### Row 1749
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1750
- Missing value(s) in column(s): addressline2, state

### Row 1751
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1752
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1753
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1754
- Missing value(s) in column(s): addressline2, territory

### Row 1755
- Missing value(s) in column(s): addressline2, territory

### Row 1756
- Missing value(s) in column(s): addressline2, state

### Row 1757
- Missing value(s) in column(s): addressline2, territory

### Row 1758
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1759
- Missing value(s) in column(s): addressline2, state

### Row 1760
- Missing value(s) in column(s): addressline2, territory

### Row 1761
- Missing value(s) in column(s): addressline2, postalcode

### Row 1762
- Missing value(s) in column(s): addressline2, state

### Row 1763
- Missing value(s) in column(s): addressline2, postalcode

### Row 1764
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1765
- Missing value(s) in column(s): addressline2, state

### Row 1766
- Missing value(s) in column(s): addressline2, state

### Row 1767
- Missing value(s) in column(s): addressline2, state

### Row 1768
- Missing value(s) in column(s): addressline2, territory

### Row 1769
- Missing value(s) in column(s): addressline2

### Row 1770
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1771
- Missing value(s) in column(s): addressline2, territory

### Row 1773
- Missing value(s) in column(s): addressline2, state

### Row 1774
- Missing value(s) in column(s): addressline2, state

### Row 1775
- Missing value(s) in column(s): addressline2, territory

### Row 1776
- Missing value(s) in column(s): addressline2, territory

### Row 1777
- Missing value(s) in column(s): territory

### Row 1778
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1779
- Missing value(s) in column(s): addressline2, state

### Row 1780
- Missing value(s) in column(s): addressline2, state

### Row 1781
- Missing value(s) in column(s): territory

### Row 1782
- Missing value(s) in column(s): addressline2, state

### Row 1783
- Missing value(s) in column(s): state

### Row 1784
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1785
- Missing value(s) in column(s): addressline2, state

### Row 1786
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1787
- Missing value(s) in column(s): addressline2, territory

### Row 1788
- Missing value(s) in column(s): addressline2, territory

### Row 1789
- Missing value(s) in column(s): addressline2, state

### Row 1790
- Missing value(s) in column(s): addressline2, territory

### Row 1792
- Missing value(s) in column(s): addressline2, territory

### Row 1793
- Missing value(s) in column(s): addressline2, state

### Row 1794
- Missing value(s) in column(s): addressline2, territory

### Row 1795
- Missing value(s) in column(s): addressline2, territory

### Row 1796
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1797
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1798
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1799
- Missing value(s) in column(s): addressline2, territory

### Row 1800
- Missing value(s) in column(s): addressline2, state

### Row 1801
- Missing value(s) in column(s): addressline2, state

### Row 1802
- Missing value(s) in column(s): addressline2, state

### Row 1803
- Missing value(s) in column(s): addressline2, state

### Row 1804
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1805
- Missing value(s) in column(s): addressline2, state

### Row 1806
- Missing value(s) in column(s): addressline2, territory

### Row 1807
- Missing value(s) in column(s): addressline2, state

### Row 1808
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1809
- Missing value(s) in column(s): addressline2, state

### Row 1810
- Missing value(s) in column(s): addressline2, territory

### Row 1811
- Missing value(s) in column(s): addressline2, territory

### Row 1813
- Missing value(s) in column(s): addressline2, state

### Row 1814
- Missing value(s) in column(s): addressline2, territory

### Row 1815
- Missing value(s) in column(s): addressline2, state

### Row 1816
- Missing value(s) in column(s): addressline2, territory

### Row 1817
- Missing value(s) in column(s): addressline2, state

### Row 1818
- Missing value(s) in column(s): addressline2, state

### Row 1819
- Missing value(s) in column(s): addressline2, state

### Row 1820
- Missing value(s) in column(s): addressline2, state

### Row 1821
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1822
- Missing value(s) in column(s): addressline2, territory

### Row 1823
- Missing value(s) in column(s): addressline2, territory

### Row 1824
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1825
- Missing value(s) in column(s): addressline2, state

### Row 1826
- Missing value(s) in column(s): addressline2, territory

### Row 1827
- Missing value(s) in column(s): addressline2, state

### Row 1828
- Missing value(s) in column(s): addressline2, state

### Row 1829
- Missing value(s) in column(s): addressline2, territory

### Row 1830
- Missing value(s) in column(s): addressline2, territory

### Row 1831
- Missing value(s) in column(s): addressline2, territory

### Row 1832
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1833
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1834
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1835
- Missing value(s) in column(s): addressline2, territory

### Row 1836
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1837
- Missing value(s) in column(s): addressline2, state

### Row 1838
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1839
- Missing value(s) in column(s): addressline2, postalcode
- Outlier in 'sales': 1.076e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 1840
- Missing value(s) in column(s): addressline2, state

### Row 1841
- Missing value(s) in column(s): addressline2, state

### Row 1842
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1843
- Missing value(s) in column(s): addressline2, territory

### Row 1844
- Missing value(s) in column(s): addressline2, territory

### Row 1845
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1846
- Missing value(s) in column(s): addressline2, territory

### Row 1848
- Missing value(s) in column(s): addressline2, state

### Row 1849
- Missing value(s) in column(s): addressline2, territory

### Row 1850
- Missing value(s) in column(s): addressline2, territory

### Row 1851
- Missing value(s) in column(s): addressline2, territory

### Row 1852
- Missing value(s) in column(s): territory

### Row 1853
- Missing value(s) in column(s): addressline2, state

### Row 1854
- Missing value(s) in column(s): addressline2, state

### Row 1855
- Missing value(s) in column(s): addressline2, state

### Row 1856
- Missing value(s) in column(s): territory

### Row 1857
- Missing value(s) in column(s): addressline2, state

### Row 1858
- Missing value(s) in column(s): state

### Row 1859
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1860
- Missing value(s) in column(s): addressline2, state

### Row 1861
- Missing value(s) in column(s): addressline2, territory

### Row 1862
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1863
- Missing value(s) in column(s): addressline2, territory

### Row 1864
- Missing value(s) in column(s): addressline2, territory

### Row 1865
- Missing value(s) in column(s): addressline2, state

### Row 1866
- Missing value(s) in column(s): addressline2, territory

### Row 1868
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1869
- Missing value(s) in column(s): addressline2, state

### Row 1870
- Missing value(s) in column(s): addressline2, territory

### Row 1871
- Missing value(s) in column(s): addressline2, territory

### Row 1872
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1874
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1875
- Missing value(s) in column(s): addressline2, state

### Row 1876
- Missing value(s) in column(s): addressline2, state

### Row 1877
- Missing value(s) in column(s): addressline2, state

### Row 1878
- Missing value(s) in column(s): addressline2, state

### Row 1879
- Missing value(s) in column(s): addressline2, state

### Row 1880
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1881
- Missing value(s) in column(s): addressline2, state

### Row 1882
- Missing value(s) in column(s): addressline2, territory

### Row 1883
- Missing value(s) in column(s): addressline2, state

### Row 1884
- Missing value(s) in column(s): addressline2, state

### Row 1885
- Missing value(s) in column(s): addressline2, state

### Row 1886
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1887
- Missing value(s) in column(s): addressline2, territory

### Row 1889
- Missing value(s) in column(s): addressline2, state

### Row 1890
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1891
- Missing value(s) in column(s): addressline2, state

### Row 1892
- Missing value(s) in column(s): addressline2, territory

### Row 1893
- Missing value(s) in column(s): addressline2, state

### Row 1894
- Missing value(s) in column(s): addressline2, state

### Row 1895
- Missing value(s) in column(s): addressline2, state

### Row 1896
- Missing value(s) in column(s): addressline2, territory

### Row 1897
- Missing value(s) in column(s): addressline2, territory

### Row 1898
- Missing value(s) in column(s): addressline2, state

### Row 1899
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1900
- Missing value(s) in column(s): addressline2, state

### Row 1901
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1902
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1903
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1904
- Missing value(s) in column(s): addressline2, territory

### Row 1905
- Missing value(s) in column(s): addressline2, territory

### Row 1906
- Missing value(s) in column(s): addressline2, state

### Row 1907
- Missing value(s) in column(s): addressline2, territory

### Row 1908
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1909
- Missing value(s) in column(s): addressline2, state

### Row 1910
- Missing value(s) in column(s): addressline2, territory

### Row 1911
- Missing value(s) in column(s): addressline2, postalcode

### Row 1912
- Missing value(s) in column(s): addressline2, state

### Row 1913
- Missing value(s) in column(s): addressline2, postalcode

### Row 1914
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1916
- Missing value(s) in column(s): addressline2, state

### Row 1917
- Missing value(s) in column(s): addressline2, state

### Row 1918
- Missing value(s) in column(s): addressline2, state

### Row 1919
- Missing value(s) in column(s): addressline2, territory

### Row 1920
- Missing value(s) in column(s): addressline2

### Row 1921
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1922
- Missing value(s) in column(s): addressline2, territory

### Row 1924
- Missing value(s) in column(s): addressline2, state

### Row 1925
- Missing value(s) in column(s): addressline2, territory

### Row 1926
- Missing value(s) in column(s): addressline2, territory

### Row 1927
- Missing value(s) in column(s): addressline2, territory

### Row 1928
- Missing value(s) in column(s): territory

### Row 1929
- Missing value(s) in column(s): addressline2, state

### Row 1930
- Missing value(s) in column(s): addressline2, territory

### Row 1931
- Missing value(s) in column(s): addressline2, state

### Row 1932
- Missing value(s) in column(s): territory

### Row 1933
- Missing value(s) in column(s): addressline2, state

### Row 1934
- Missing value(s) in column(s): state

### Row 1935
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1936
- Missing value(s) in column(s): addressline2, state

### Row 1937
- Missing value(s) in column(s): addressline2, territory

### Row 1938
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1939
- Missing value(s) in column(s): addressline2, territory

### Row 1940
- Missing value(s) in column(s): addressline2, territory

### Row 1941
- Missing value(s) in column(s): addressline2, state

### Row 1942
- Missing value(s) in column(s): addressline2, territory

### Row 1944
- Missing value(s) in column(s): addressline2, state

### Row 1945
- Missing value(s) in column(s): addressline2, state

### Row 1946
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1947
- Missing value(s) in column(s): addressline2, territory

### Row 1948
- Missing value(s) in column(s): addressline2, state

### Row 1949
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1950
- Missing value(s) in column(s): addressline2, state

### Row 1951
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1952
- Missing value(s) in column(s): addressline2, state

### Row 1953
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1954
- Missing value(s) in column(s): addressline2, territory

### Row 1955
- Missing value(s) in column(s): addressline2, territory

### Row 1956
- Missing value(s) in column(s): addressline2, state

### Row 1957
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1958
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1959
- Missing value(s) in column(s): addressline2, state

### Row 1960
- Missing value(s) in column(s): addressline2, territory

### Row 1961
- Missing value(s) in column(s): addressline2, postalcode

### Row 1962
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1963
- Missing value(s) in column(s): addressline2, postalcode

### Row 1964
- Missing value(s) in column(s): addressline2, state

### Row 1965
- Missing value(s) in column(s): addressline2, state

### Row 1966
- Missing value(s) in column(s): addressline2, territory

### Row 1967
- Missing value(s) in column(s): addressline2, territory

### Row 1968
- Missing value(s) in column(s): addressline2, territory

### Row 1969
- Missing value(s) in column(s): addressline2, territory

### Row 1970
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1971
- Missing value(s) in column(s): addressline2, state

### Row 1972
- Missing value(s) in column(s): addressline2, territory

### Row 1973
- Missing value(s) in column(s): addressline2, territory

### Row 1974
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 1975
- Missing value(s) in column(s): addressline2, state

### Row 1976
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1977
- Missing value(s) in column(s): addressline2, territory

### Row 1978
- Missing value(s) in column(s): addressline2, state

### Row 1979
- Missing value(s) in column(s): addressline2, state

### Row 1980
- Missing value(s) in column(s): addressline2, state

### Row 1981
- Missing value(s) in column(s): addressline2, state

### Row 1982
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1983
- Missing value(s) in column(s): addressline2, state

### Row 1984
- Missing value(s) in column(s): addressline2, territory

### Row 1985
- Missing value(s) in column(s): addressline2, state

### Row 1986
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1987
- Missing value(s) in column(s): addressline2, state

### Row 1988
- Missing value(s) in column(s): addressline2, territory

### Row 1989
- Missing value(s) in column(s): addressline2, territory

### Row 1991
- Missing value(s) in column(s): addressline2, state

### Row 1992
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 1993
- Missing value(s) in column(s): addressline2, state

### Row 1994
- Missing value(s) in column(s): addressline2, territory

### Row 1995
- Missing value(s) in column(s): addressline2, state
- Outlier in 'quantityordered': 76 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])
- Outlier in 'sales': 1.174e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 1996
- Missing value(s) in column(s): addressline2, state
- Outlier in 'quantityordered': 70 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])
- Outlier in 'sales': 9240 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 1997
- Missing value(s) in column(s): addressline2, state

### Row 1998
- Missing value(s) in column(s): addressline2, state

### Row 1999
- Missing value(s) in column(s): addressline2, territory

### Row 2000
- Missing value(s) in column(s): addressline2, territory

### Row 2001
- Missing value(s) in column(s): addressline2, state

### Row 2002
- Missing value(s) in column(s): addressline2, territory

### Row 2003
- Missing value(s) in column(s): addressline2, state

### Row 2004
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2005
- Missing value(s) in column(s): addressline2, postalcode

### Row 2006
- Missing value(s) in column(s): addressline2, territory

### Row 2007
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2008
- Missing value(s) in column(s): addressline2, territory

### Row 2009
- Missing value(s) in column(s): addressline2, state

### Row 2010
- Missing value(s) in column(s): addressline2, state

### Row 2011
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2012
- Missing value(s) in column(s): addressline2, state

### Row 2013
- Missing value(s) in column(s): addressline2, territory

### Row 2014
- Missing value(s) in column(s): addressline2, postalcode

### Row 2015
- Missing value(s) in column(s): addressline2, state

### Row 2016
- Missing value(s) in column(s): addressline2, postalcode

### Row 2017
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2019
- Missing value(s) in column(s): addressline2, state

### Row 2020
- Missing value(s) in column(s): addressline2, state

### Row 2021
- Missing value(s) in column(s): addressline2, state

### Row 2022
- Missing value(s) in column(s): addressline2, territory

### Row 2023
- Missing value(s) in column(s): addressline2, state

### Row 2024
- Missing value(s) in column(s): addressline2, territory

### Row 2025
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2026
- Missing value(s) in column(s): addressline2, territory

### Row 2027
- Missing value(s) in column(s): addressline2, territory

### Row 2028
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2029
- Missing value(s) in column(s): addressline2, state

### Row 2030
- Missing value(s) in column(s): addressline2, territory

### Row 2031
- Missing value(s) in column(s): addressline2

### Row 2032
- Missing value(s) in column(s): territory

### Row 2033
- Missing value(s) in column(s): addressline2, state

### Row 2034
- Missing value(s) in column(s): addressline2, state

### Row 2035
- Missing value(s) in column(s): territory

### Row 2036
- Missing value(s) in column(s): addressline2, state

### Row 2037
- Missing value(s) in column(s): state

### Row 2038
- Missing value(s) in column(s): addressline2, state

### Row 2039
- Missing value(s) in column(s): addressline2, territory

### Row 2040
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2041
- Missing value(s) in column(s): addressline2, territory

### Row 2042
- Missing value(s) in column(s): addressline2, territory

### Row 2043
- Missing value(s) in column(s): addressline2, state

### Row 2044
- Missing value(s) in column(s): addressline2, postalcode

### Row 2046
- Missing value(s) in column(s): addressline2, state

### Row 2047
- Missing value(s) in column(s): territory

### Row 2048
- Missing value(s) in column(s): territory

### Row 2049
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2050
- Missing value(s) in column(s): addressline2

### Row 2051
- Missing value(s) in column(s): addressline2, state

### Row 2052
- Missing value(s) in column(s): addressline2, state

### Row 2053
- Missing value(s) in column(s): addressline2, state

### Row 2054
- Missing value(s) in column(s): addressline2, territory

### Row 2055
- Missing value(s) in column(s): addressline2, territory

### Row 2056
- Missing value(s) in column(s): state

### Row 2057
- Missing value(s) in column(s): addressline2, state

### Row 2058
- Missing value(s) in column(s): addressline2, state

### Row 2059
- Missing value(s) in column(s): addressline2, territory

### Row 2060
- Missing value(s) in column(s): addressline2, territory

### Row 2061
- Missing value(s) in column(s): addressline2, territory

### Row 2062
- Missing value(s) in column(s): addressline2, territory

### Row 2063
- Missing value(s) in column(s): addressline2, state

### Row 2064
- Missing value(s) in column(s): addressline2, state

### Row 2065
- Missing value(s) in column(s): addressline2, state

### Row 2066
- Missing value(s) in column(s): territory

### Row 2067
- Missing value(s) in column(s): addressline2, state

### Row 2068
- Missing value(s) in column(s): addressline2, territory

### Row 2069
- Missing value(s) in column(s): addressline2, state

### Row 2070
- Missing value(s) in column(s): addressline2, state

### Row 2071
- Missing value(s) in column(s): addressline2, state

### Row 2072
- Missing value(s) in column(s): addressline2, state

### Row 2073
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2074
- Missing value(s) in column(s): addressline2, state

### Row 2076
- Missing value(s) in column(s): addressline2, territory

### Row 2077
- Missing value(s) in column(s): territory

### Row 2078
- Missing value(s) in column(s): addressline2, state

### Row 2079
- Missing value(s) in column(s): addressline2, territory

### Row 2080
- Missing value(s) in column(s): addressline2

### Row 2081
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2082
- Missing value(s) in column(s): addressline2, territory

### Row 2083
- Missing value(s) in column(s): addressline2, territory

### Row 2084
- Missing value(s) in column(s): addressline2, state

### Row 2085
- Missing value(s) in column(s): addressline2, territory

### Row 2086
- Missing value(s) in column(s): addressline2, state

### Row 2087
- Missing value(s) in column(s): addressline2, state

### Row 2088
- Missing value(s) in column(s): addressline2, territory

### Row 2089
- Missing value(s) in column(s): addressline2, state

### Row 2090
- Missing value(s) in column(s): addressline2, territory

### Row 2091
- Missing value(s) in column(s): territory

### Row 2092
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2093
- Missing value(s) in column(s): addressline2, state

### Row 2094
- Missing value(s) in column(s): addressline2, state

### Row 2095
- Missing value(s) in column(s): addressline2, territory

### Row 2096
- Missing value(s) in column(s): addressline2, territory

### Row 2097
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2098
- Missing value(s) in column(s): addressline2, state

### Row 2100
- Missing value(s) in column(s): addressline2, state

### Row 2101
- Missing value(s) in column(s): addressline2, territory

### Row 2102
- Missing value(s) in column(s): addressline2, territory

### Row 2103
- Missing value(s) in column(s): addressline2, postalcode

### Row 2105
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2106
- Missing value(s) in column(s): addressline2, territory

### Row 2107
- Missing value(s) in column(s): addressline2, territory

### Row 2108
- Missing value(s) in column(s): addressline2, state

### Row 2109
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2110
- Missing value(s) in column(s): state

### Row 2111
- Missing value(s) in column(s): addressline2, territory

### Row 2112
- Missing value(s) in column(s): addressline2, territory

### Row 2113
- Missing value(s) in column(s): addressline2, state

### Row 2114
- Missing value(s) in column(s): addressline2, state

### Row 2115
- Missing value(s) in column(s): addressline2, territory

### Row 2117
- Missing value(s) in column(s): addressline2, state
- Outlier in 'sales': 1.004e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 2118
- Missing value(s) in column(s): addressline2, state

### Row 2119
- Missing value(s) in column(s): addressline2, state

### Row 2120
- Missing value(s) in column(s): addressline2, territory

### Row 2121
- Missing value(s) in column(s): addressline2, state

### Row 2122
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2123
- Missing value(s) in column(s): addressline2, state

### Row 2124
- Missing value(s) in column(s): addressline2, territory

### Row 2125
- Missing value(s) in column(s): addressline2, territory

### Row 2126
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2128
- Missing value(s) in column(s): addressline2, state

### Row 2129
- Missing value(s) in column(s): addressline2, state

### Row 2130
- Missing value(s) in column(s): addressline2, state

### Row 2131
- Missing value(s) in column(s): addressline2, state

### Row 2132
- Missing value(s) in column(s): addressline2, state

### Row 2133
- Missing value(s) in column(s): addressline2, state

### Row 2134
- Missing value(s) in column(s): addressline2, territory

### Row 2135
- Missing value(s) in column(s): addressline2, territory

### Row 2136
- Missing value(s) in column(s): addressline2, state

### Row 2137
- Missing value(s) in column(s): addressline2, state

### Row 2138
- Missing value(s) in column(s): addressline2, state

### Row 2139
- Missing value(s) in column(s): territory

### Row 2140
- Missing value(s) in column(s): addressline2, territory

### Row 2141
- Missing value(s) in column(s): addressline2, state

### Row 2142
- Missing value(s) in column(s): addressline2, state

### Row 2143
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2144
- Missing value(s) in column(s): addressline2, state

### Row 2145
- Missing value(s) in column(s): addressline2, territory

### Row 2146
- Missing value(s) in column(s): addressline2, state

### Row 2147
- Missing value(s) in column(s): addressline2, state

### Row 2148
- Missing value(s) in column(s): addressline2, state

### Row 2149
- Missing value(s) in column(s): addressline2, territory

### Row 2150
- Missing value(s) in column(s): addressline2, state

### Row 2151
- Missing value(s) in column(s): addressline2, state

### Row 2152
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2153
- Missing value(s) in column(s): addressline2, state

### Row 2154
- Missing value(s) in column(s): addressline2, state

### Row 2155
- Missing value(s) in column(s): addressline2, territory

### Row 2156
- Missing value(s) in column(s): state

### Row 2157
- Missing value(s) in column(s): addressline2, territory

### Row 2158
- Missing value(s) in column(s): addressline2, territory

### Row 2159
- Missing value(s) in column(s): state

### Row 2161
- Missing value(s) in column(s): addressline2, territory

### Row 2162
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2163
- Missing value(s) in column(s): addressline2, territory

### Row 2164
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2165
- Missing value(s) in column(s): territory

### Row 2166
- Missing value(s) in column(s): addressline2, territory

### Row 2167
- Missing value(s) in column(s): addressline2, state

### Row 2168
- Missing value(s) in column(s): addressline2, state

### Row 2169
- Missing value(s) in column(s): addressline2, territory

### Row 2170
- Missing value(s) in column(s): addressline2, territory

### Row 2171
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2172
- Missing value(s) in column(s): addressline2, state

### Row 2173
- Missing value(s) in column(s): addressline2, territory

### Row 2175
- Missing value(s) in column(s): addressline2, state

### Row 2176
- Missing value(s) in column(s): addressline2, territory

### Row 2177
- Missing value(s) in column(s): addressline2, territory

### Row 2178
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2179
- Missing value(s) in column(s): addressline2, postalcode

### Row 2181
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2182
- Missing value(s) in column(s): addressline2, territory

### Row 2183
- Missing value(s) in column(s): addressline2, territory

### Row 2184
- Missing value(s) in column(s): addressline2, state

### Row 2185
- Missing value(s) in column(s): addressline2, territory

### Row 2186
- Missing value(s) in column(s): state

### Row 2187
- Missing value(s) in column(s): addressline2, territory

### Row 2188
- Missing value(s) in column(s): addressline2, territory

### Row 2189
- Missing value(s) in column(s): addressline2, territory

### Row 2190
- Missing value(s) in column(s): addressline2, state

### Row 2191
- Missing value(s) in column(s): addressline2, territory

### Row 2192
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2193
- Missing value(s) in column(s): addressline2, state

### Row 2194
- Missing value(s) in column(s): addressline2, state

### Row 2195
- Missing value(s) in column(s): addressline2, territory

### Row 2196
- Missing value(s) in column(s): addressline2, state

### Row 2197
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2198
- Missing value(s) in column(s): addressline2, state

### Row 2199
- Missing value(s) in column(s): addressline2, territory

### Row 2200
- Missing value(s) in column(s): addressline2, territory

### Row 2201
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2203
- Missing value(s) in column(s): addressline2, state

### Row 2204
- Missing value(s) in column(s): addressline2, state

### Row 2205
- Missing value(s) in column(s): addressline2, state

### Row 2206
- Missing value(s) in column(s): addressline2, state

### Row 2207
- Missing value(s) in column(s): territory

### Row 2208
- Missing value(s) in column(s): addressline2, state

### Row 2209
- Missing value(s) in column(s): addressline2, territory

### Row 2210
- Missing value(s) in column(s): addressline2, territory

### Row 2211
- Missing value(s) in column(s): addressline2, territory

### Row 2212
- Missing value(s) in column(s): addressline2, state

### Row 2213
- Missing value(s) in column(s): addressline2, state

### Row 2214
- Missing value(s) in column(s): territory

### Row 2215
- Missing value(s) in column(s): addressline2, territory

### Row 2216
- Missing value(s) in column(s): addressline2, state

### Row 2217
- Missing value(s) in column(s): addressline2, state

### Row 2218
- Missing value(s) in column(s): addressline2, state

### Row 2219
- Missing value(s) in column(s): addressline2, state

### Row 2220
- Missing value(s) in column(s): addressline2, territory

### Row 2221
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2222
- Missing value(s) in column(s): addressline2, state

### Row 2223
- Missing value(s) in column(s): addressline2, state

### Row 2224
- Missing value(s) in column(s): territory

### Row 2225
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2226
- Missing value(s) in column(s): addressline2, state

### Row 2227
- Missing value(s) in column(s): addressline2, state

### Row 2228
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2229
- Missing value(s) in column(s): addressline2, state

### Row 2230
- Missing value(s) in column(s): addressline2, territory

### Row 2231
- Missing value(s) in column(s): addressline2, territory

### Row 2232
- Missing value(s) in column(s): addressline2, territory

### Row 2233
- Missing value(s) in column(s): addressline2, territory

### Row 2234
- Missing value(s) in column(s): addressline2, state

### Row 2235
- Missing value(s) in column(s): state

### Row 2236
- Missing value(s) in column(s): addressline2, territory

### Row 2237
- Missing value(s) in column(s): addressline2, territory

### Row 2238
- Missing value(s) in column(s): addressline2, territory

### Row 2239
- Missing value(s) in column(s): addressline2, territory

### Row 2240
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2241
- Missing value(s) in column(s): addressline2, state

### Row 2242
- Missing value(s) in column(s): addressline2, territory

### Row 2243
- Missing value(s) in column(s): territory

### Row 2244
- Missing value(s) in column(s): addressline2, state

### Row 2245
- Missing value(s) in column(s): addressline2, territory

### Row 2246
- Missing value(s) in column(s): addressline2, state

### Row 2247
- Missing value(s) in column(s): addressline2, state

### Row 2248
- Missing value(s) in column(s): addressline2, state

### Row 2249
- Missing value(s) in column(s): addressline2, state

### Row 2250
- Missing value(s) in column(s): addressline2, state

### Row 2251
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2252
- Missing value(s) in column(s): territory

### Row 2253
- Missing value(s) in column(s): addressline2, territory

### Row 2254
- Missing value(s) in column(s): addressline2

### Row 2255
- Missing value(s) in column(s): addressline2, state

### Row 2256
- Missing value(s) in column(s): addressline2, state

### Row 2257
- Missing value(s) in column(s): addressline2, state

### Row 2258
- Missing value(s) in column(s): addressline2, territory

### Row 2259
- Missing value(s) in column(s): addressline2, territory

### Row 2260
- Missing value(s) in column(s): state

### Row 2261
- Missing value(s) in column(s): addressline2, state

### Row 2262
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2263
- Missing value(s) in column(s): addressline2, territory

### Row 2264
- Missing value(s) in column(s): addressline2, territory

### Row 2265
- Missing value(s) in column(s): addressline2, territory

### Row 2266
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2267
- Missing value(s) in column(s): addressline2, state

### Row 2268
- Missing value(s) in column(s): addressline2, state

### Row 2269
- Missing value(s) in column(s): addressline2, state

### Row 2270
- Missing value(s) in column(s): addressline2, state

### Row 2271
- Missing value(s) in column(s): addressline2, state

### Row 2272
- Missing value(s) in column(s): addressline2, territory

### Row 2273
- Missing value(s) in column(s): addressline2, state

### Row 2274
- Missing value(s) in column(s): addressline2, state

### Row 2275
- Missing value(s) in column(s): addressline2, territory

### Row 2276
- Missing value(s) in column(s): addressline2, state

### Row 2277
- Missing value(s) in column(s): addressline2, territory

### Row 2278
- Missing value(s) in column(s): addressline2, state

### Row 2279
- Missing value(s) in column(s): addressline2, territory

### Row 2280
- Missing value(s) in column(s): addressline2, state

### Row 2281
- Missing value(s) in column(s): addressline2, state

### Row 2282
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2283
- Missing value(s) in column(s): addressline2, territory

### Row 2284
- Missing value(s) in column(s): addressline2, state

### Row 2285
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2286
- Missing value(s) in column(s): state

### Row 2287
- Missing value(s) in column(s): addressline2, territory

### Row 2288
- Missing value(s) in column(s): addressline2, territory

### Row 2289
- Missing value(s) in column(s): addressline2, postalcode

### Row 2291
- Missing value(s) in column(s): addressline2, territory

### Row 2292
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2293
- Missing value(s) in column(s): addressline2, state

### Row 2294
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2295
- Missing value(s) in column(s): territory

### Row 2296
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2297
- Missing value(s) in column(s): addressline2, state

### Row 2298
- Missing value(s) in column(s): addressline2, state

### Row 2300
- Missing value(s) in column(s): addressline2, territory

### Row 2301
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2302
- Missing value(s) in column(s): addressline2, state

### Row 2303
- Missing value(s) in column(s): addressline2, state

### Row 2305
- Missing value(s) in column(s): addressline2, state

### Row 2306
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2307
- Missing value(s) in column(s): addressline2, territory

### Row 2308
- Missing value(s) in column(s): addressline2, postalcode

### Row 2310
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2311
- Missing value(s) in column(s): addressline2, territory

### Row 2312
- Missing value(s) in column(s): addressline2, state

### Row 2313
- Missing value(s) in column(s): addressline2, state

### Row 2314
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2315
- Missing value(s) in column(s): state

### Row 2316
- Missing value(s) in column(s): addressline2, territory

### Row 2317
- Missing value(s) in column(s): addressline2, postalcode

### Row 2318
- Missing value(s) in column(s): addressline2, state

### Row 2319
- Missing value(s) in column(s): addressline2, state

### Row 2320
- Missing value(s) in column(s): addressline2, territory

### Row 2322
- Missing value(s) in column(s): addressline2, state

### Row 2323
- Missing value(s) in column(s): addressline2, territory

### Row 2324
- Missing value(s) in column(s): addressline2, state

### Row 2325
- Missing value(s) in column(s): addressline2, territory

### Row 2326
- Missing value(s) in column(s): addressline2, state

### Row 2327
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2328
- Missing value(s) in column(s): addressline2, state

### Row 2329
- Missing value(s) in column(s): addressline2, territory

### Row 2330
- Missing value(s) in column(s): addressline2, territory

### Row 2331
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2333
- Missing value(s) in column(s): addressline2, state

### Row 2334
- Missing value(s) in column(s): addressline2, state

### Row 2335
- Missing value(s) in column(s): addressline2, state

### Row 2336
- Missing value(s) in column(s): addressline2, state

### Row 2337
- Missing value(s) in column(s): territory

### Row 2338
- Missing value(s) in column(s): addressline2, state

### Row 2339
- Missing value(s) in column(s): addressline2, territory

### Row 2340
- Missing value(s) in column(s): addressline2, territory

### Row 2341
- Missing value(s) in column(s): addressline2, territory

### Row 2342
- Missing value(s) in column(s): addressline2, state

### Row 2343
- Missing value(s) in column(s): addressline2, state

### Row 2344
- Missing value(s) in column(s): territory

### Row 2345
- Missing value(s) in column(s): addressline2, territory

### Row 2346
- Missing value(s) in column(s): addressline2, state

### Row 2347
- Missing value(s) in column(s): addressline2, state

### Row 2348
- Missing value(s) in column(s): addressline2, territory

### Row 2349
- Missing value(s) in column(s): addressline2, state

### Row 2350
- Missing value(s) in column(s): addressline2, territory

### Row 2351
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2352
- Missing value(s) in column(s): addressline2, state

### Row 2354
- Missing value(s) in column(s): addressline2, state

### Row 2355
- Missing value(s) in column(s): addressline2, territory

### Row 2356
- Missing value(s) in column(s): addressline2, state

### Row 2357
- Missing value(s) in column(s): addressline2, territory

### Row 2358
- Missing value(s) in column(s): addressline2, territory

### Row 2359
- Missing value(s) in column(s): addressline2, postalcode

### Row 2361
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2362
- Missing value(s) in column(s): addressline2, territory

### Row 2363
- Missing value(s) in column(s): addressline2, state

### Row 2364
- Missing value(s) in column(s): addressline2, state

### Row 2365
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2366
- Missing value(s) in column(s): addressline2, state

### Row 2367
- Missing value(s) in column(s): addressline2, territory

### Row 2368
- Missing value(s) in column(s): addressline2, postalcode

### Row 2369
- Missing value(s) in column(s): addressline2, state

### Row 2370
- Missing value(s) in column(s): addressline2, state

### Row 2371
- Missing value(s) in column(s): addressline2, territory

### Row 2373
- Missing value(s) in column(s): addressline2, state

### Row 2374
- Missing value(s) in column(s): addressline2, territory

### Row 2375
- Missing value(s) in column(s): addressline2, state

### Row 2376
- Missing value(s) in column(s): addressline2, territory

### Row 2377
- Missing value(s) in column(s): addressline2, state

### Row 2378
- Missing value(s) in column(s): addressline2, state

### Row 2379
- Missing value(s) in column(s): territory

### Row 2380
- Missing value(s) in column(s): territory

### Row 2381
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2382
- Missing value(s) in column(s): addressline2, state

### Row 2383
- Missing value(s) in column(s): addressline2, state

### Row 2384
- Missing value(s) in column(s): addressline2, state

### Row 2385
- Missing value(s) in column(s): addressline2, state

### Row 2386
- Missing value(s) in column(s): addressline2, territory

### Row 2387
- Missing value(s) in column(s): addressline2, territory

### Row 2388
- Missing value(s) in column(s): state

### Row 2389
- Missing value(s) in column(s): addressline2, state

### Row 2390
- Missing value(s) in column(s): addressline2, state

### Row 2391
- Missing value(s) in column(s): state

### Row 2392
- Missing value(s) in column(s): addressline2, territory

### Row 2393
- Missing value(s) in column(s): addressline2, territory

### Row 2394
- Missing value(s) in column(s): addressline2, territory

### Row 2395
- Missing value(s) in column(s): addressline2, territory

### Row 2396
- Missing value(s) in column(s): addressline2, state

### Row 2397
- Missing value(s) in column(s): addressline2, state

### Row 2398
- Missing value(s) in column(s): addressline2, state

### Row 2399
- Missing value(s) in column(s): addressline2, state

### Row 2400
- Missing value(s) in column(s): addressline2, state

### Row 2401
- Missing value(s) in column(s): addressline2, territory

### Row 2402
- Missing value(s) in column(s): addressline2, state

### Row 2403
- Missing value(s) in column(s): addressline2, state

### Row 2404
- Missing value(s) in column(s): addressline2, state

### Row 2405
- Missing value(s) in column(s): addressline2, state

### Row 2406
- Missing value(s) in column(s): addressline2, state

### Row 2407
- Missing value(s) in column(s): addressline2, state

### Row 2408
- Missing value(s) in column(s): territory

### Row 2409
- Missing value(s) in column(s): addressline2, territory

### Row 2410
- Missing value(s) in column(s): addressline2, state

### Row 2411
- Missing value(s) in column(s): addressline2, state

### Row 2412
- Missing value(s) in column(s): addressline2, state

### Row 2413
- Missing value(s) in column(s): addressline2, territory

### Row 2414
- Missing value(s) in column(s): addressline2, territory

### Row 2415
- Missing value(s) in column(s): addressline2, state

### Row 2416
- Missing value(s) in column(s): state

### Row 2417
- Missing value(s) in column(s): addressline2, state

### Row 2418
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2419
- Missing value(s) in column(s): addressline2, territory

### Row 2420
- Missing value(s) in column(s): addressline2, territory

### Row 2421
- Missing value(s) in column(s): addressline2, territory

### Row 2422
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2423
- Missing value(s) in column(s): addressline2, state

### Row 2424
- Missing value(s) in column(s): addressline2, state

### Row 2425
- Missing value(s) in column(s): territory

### Row 2426
- Missing value(s) in column(s): addressline2, state

### Row 2427
- Missing value(s) in column(s): addressline2, state

### Row 2428
- Missing value(s) in column(s): addressline2, postalcode

### Row 2429
- Missing value(s) in column(s): addressline2, state

### Row 2430
- Missing value(s) in column(s): addressline2, state

### Row 2431
- Missing value(s) in column(s): addressline2, territory

### Row 2432
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2433
- Missing value(s) in column(s): addressline2, state

### Row 2434
- Missing value(s) in column(s): addressline2, territory

### Row 2435
- Missing value(s) in column(s): addressline2, territory

### Row 2436
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2438
- Missing value(s) in column(s): addressline2, state

### Row 2439
- Missing value(s) in column(s): addressline2, state

### Row 2440
- Missing value(s) in column(s): addressline2, state

### Row 2441
- Missing value(s) in column(s): addressline2, state

### Row 2442
- Missing value(s) in column(s): territory

### Row 2443
- Missing value(s) in column(s): addressline2, state

### Row 2444
- Missing value(s) in column(s): addressline2, territory

### Row 2445
- Missing value(s) in column(s): addressline2, territory

### Row 2446
- Missing value(s) in column(s): addressline2, territory

### Row 2447
- Missing value(s) in column(s): addressline2, state

### Row 2448
- Missing value(s) in column(s): addressline2, state

### Row 2449
- Missing value(s) in column(s): territory

### Row 2450
- Missing value(s) in column(s): addressline2, territory

### Row 2451
- Missing value(s) in column(s): addressline2, state

### Row 2452
- Missing value(s) in column(s): addressline2, state

### Row 2453
- Missing value(s) in column(s): addressline2, territory

### Row 2454
- Missing value(s) in column(s): addressline2, state

### Row 2455
- Missing value(s) in column(s): addressline2, territory

### Row 2456
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2457
- Missing value(s) in column(s): addressline2, state

### Row 2458
- Missing value(s) in column(s): addressline2, state

### Row 2459
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2460
- Missing value(s) in column(s): addressline2, territory

### Row 2461
- Missing value(s) in column(s): addressline2, state

### Row 2462
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2463
- Missing value(s) in column(s): addressline2, state

### Row 2464
- Missing value(s) in column(s): addressline2, territory

### Row 2465
- Missing value(s) in column(s): addressline2, state

### Row 2466
- Missing value(s) in column(s): addressline2, state

### Row 2467
- Missing value(s) in column(s): addressline2, territory

### Row 2468
- Missing value(s) in column(s): addressline2, territory

### Row 2469
- Missing value(s) in column(s): addressline2, territory

### Row 2470
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2471
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2472
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2473
- Missing value(s) in column(s): addressline2, territory

### Row 2474
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2475
- Missing value(s) in column(s): addressline2, state

### Row 2476
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2477
- Missing value(s) in column(s): addressline2, postalcode

### Row 2478
- Missing value(s) in column(s): addressline2, state

### Row 2479
- Missing value(s) in column(s): addressline2, state

### Row 2480
- Missing value(s) in column(s): addressline2, territory

### Row 2481
- Missing value(s) in column(s): addressline2, territory

### Row 2482
- Missing value(s) in column(s): addressline2, territory

### Row 2483
- Missing value(s) in column(s): addressline2, state

### Row 2485
- Missing value(s) in column(s): addressline2, state

### Row 2486
- Missing value(s) in column(s): addressline2, territory

### Row 2487
- Missing value(s) in column(s): addressline2, state

### Row 2488
- Missing value(s) in column(s): addressline2, territory

### Row 2489
- Missing value(s) in column(s): addressline2, territory

### Row 2490
- Missing value(s) in column(s): addressline2, postalcode

### Row 2492
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2493
- Missing value(s) in column(s): addressline2, territory

### Row 2494
- Missing value(s) in column(s): addressline2, state

### Row 2495
- Missing value(s) in column(s): addressline2, state

### Row 2496
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2497
- Missing value(s) in column(s): addressline2, state

### Row 2498
- Missing value(s) in column(s): addressline2, territory

### Row 2499
- Missing value(s) in column(s): addressline2, postalcode

### Row 2500
- Missing value(s) in column(s): addressline2, state

### Row 2501
- Missing value(s) in column(s): addressline2, state

### Row 2502
- Missing value(s) in column(s): addressline2, territory

### Row 2504
- Missing value(s) in column(s): addressline2, state

### Row 2505
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'sales': 1.007e+04 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 2506
- Missing value(s) in column(s): addressline2, state

### Row 2507
- Missing value(s) in column(s): addressline2, territory

### Row 2508
- Missing value(s) in column(s): addressline2, state

### Row 2509
- Missing value(s) in column(s): addressline2, state

### Row 2510
- Missing value(s) in column(s): addressline2, state

### Row 2511
- Missing value(s) in column(s): addressline2, state

### Row 2512
- Missing value(s) in column(s): addressline2, territory

### Row 2513
- Missing value(s) in column(s): addressline2, state

### Row 2514
- Missing value(s) in column(s): addressline2, territory

### Row 2515
- Missing value(s) in column(s): addressline2, state

### Row 2516
- Missing value(s) in column(s): addressline2, territory

### Row 2517
- Missing value(s) in column(s): addressline2, territory

### Row 2518
- Missing value(s) in column(s): addressline2, state

### Row 2519
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2520
- Missing value(s) in column(s): addressline2, postalcode

### Row 2521
- Missing value(s) in column(s): addressline2, territory

### Row 2522
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2523
- Missing value(s) in column(s): addressline2, territory

### Row 2524
- Missing value(s) in column(s): addressline2, state

### Row 2525
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2526
- Missing value(s) in column(s): addressline2, state

### Row 2527
- Missing value(s) in column(s): addressline2, state

### Row 2528
- Missing value(s) in column(s): territory

### Row 2529
- Missing value(s) in column(s): addressline2, state

### Row 2530
- Missing value(s) in column(s): addressline2, postalcode

### Row 2531
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2532
- Missing value(s) in column(s): addressline2, state

### Row 2533
- Missing value(s) in column(s): addressline2, territory

### Row 2534
- Missing value(s) in column(s): addressline2, state

### Row 2535
- Missing value(s) in column(s): addressline2, state

### Row 2536
- Missing value(s) in column(s): addressline2, territory

### Row 2537
- Missing value(s) in column(s): addressline2, territory

### Row 2538
- Missing value(s) in column(s): addressline2, state

### Row 2539
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2540
- Missing value(s) in column(s): addressline2, state

### Row 2541
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2542
- Missing value(s) in column(s): addressline2, state

### Row 2543
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2544
- Missing value(s) in column(s): addressline2, territory

### Row 2545
- Missing value(s) in column(s): addressline2, territory

### Row 2546
- Missing value(s) in column(s): addressline2, state

### Row 2547
- Missing value(s) in column(s): addressline2, territory

### Row 2548
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2549
- Missing value(s) in column(s): addressline2, state

### Row 2550
- Missing value(s) in column(s): addressline2, territory

### Row 2551
- Missing value(s) in column(s): addressline2, postalcode

### Row 2552
- Missing value(s) in column(s): addressline2, state

### Row 2553
- Missing value(s) in column(s): addressline2, postalcode

### Row 2554
- Missing value(s) in column(s): addressline2, territory

### Row 2556
- Missing value(s) in column(s): addressline2, state

### Row 2557
- Missing value(s) in column(s): addressline2, state

### Row 2558
- Missing value(s) in column(s): addressline2, state

### Row 2559
- Missing value(s) in column(s): addressline2, territory

### Row 2560
- Missing value(s) in column(s): addressline2

### Row 2561
- Missing value(s) in column(s): addressline2, state

### Row 2563
- Missing value(s) in column(s): addressline2, territory

### Row 2564
- Missing value(s) in column(s): addressline2, territory

### Row 2565
- Missing value(s) in column(s): addressline2, state

### Row 2566
- Missing value(s) in column(s): addressline2, territory

### Row 2567
- Missing value(s) in column(s): addressline2, state

### Row 2568
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2569
- Missing value(s) in column(s): addressline2, postalcode

### Row 2570
- Missing value(s) in column(s): addressline2, territory

### Row 2571
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2572
- Missing value(s) in column(s): addressline2, territory

### Row 2573
- Missing value(s) in column(s): addressline2, state

### Row 2574
- Missing value(s) in column(s): addressline2, state

### Row 2575
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2576
- Missing value(s) in column(s): addressline2, state

### Row 2577
- Missing value(s) in column(s): addressline2, territory

### Row 2578
- Missing value(s) in column(s): addressline2, postalcode

### Row 2579
- Missing value(s) in column(s): addressline2, state

### Row 2580
- Missing value(s) in column(s): addressline2, state

### Row 2581
- Missing value(s) in column(s): addressline2, territory

### Row 2583
- Missing value(s) in column(s): addressline2, state

### Row 2584
- Missing value(s) in column(s): addressline2, state

### Row 2585
- Missing value(s) in column(s): addressline2, state

### Row 2586
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'quantityordered': 85 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])

### Row 2587
- Missing value(s) in column(s): addressline2, state

### Row 2588
- Missing value(s) in column(s): addressline2, state

### Row 2589
- Missing value(s) in column(s): addressline2, state

### Row 2590
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2591
- Missing value(s) in column(s): addressline2, territory

### Row 2592
- Missing value(s) in column(s): addressline2, territory

### Row 2593
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2594
- Missing value(s) in column(s): addressline2, state

### Row 2595
- Missing value(s) in column(s): addressline2, territory

### Row 2596
- Missing value(s) in column(s): addressline2, state

### Row 2597
- Missing value(s) in column(s): addressline2, state

### Row 2598
- Missing value(s) in column(s): addressline2, territory

### Row 2599
- Missing value(s) in column(s): addressline2, territory

### Row 2600
- Missing value(s) in column(s): addressline2, territory

### Row 2601
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2602
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2603
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2604
- Missing value(s) in column(s): addressline2, territory

### Row 2605
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2606
- Missing value(s) in column(s): addressline2, postalcode

### Row 2607
- Missing value(s) in column(s): addressline2, state

### Row 2608
- Missing value(s) in column(s): addressline2, postalcode

### Row 2609
- Missing value(s) in column(s): addressline2, state

### Row 2610
- Missing value(s) in column(s): addressline2, state

### Row 2611
- Missing value(s) in column(s): addressline2, state

### Row 2612
- Missing value(s) in column(s): addressline2, state

### Row 2613
- Missing value(s) in column(s): addressline2, territory

### Row 2614
- Missing value(s) in column(s): addressline2, state

### Row 2615
- Missing value(s) in column(s): addressline2, state

### Row 2616
- Missing value(s) in column(s): addressline2, state

### Row 2617
- Missing value(s) in column(s): addressline2, territory

### Row 2618
- Missing value(s) in column(s): addressline2, state

### Row 2619
- Missing value(s) in column(s): addressline2, state

### Row 2620
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2621
- Missing value(s) in column(s): addressline2, territory

### Row 2622
- Missing value(s) in column(s): addressline2, state

### Row 2623
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2624
- Missing value(s) in column(s): state

### Row 2625
- Missing value(s) in column(s): addressline2, territory

### Row 2626
- Missing value(s) in column(s): addressline2, territory

### Row 2627
- Missing value(s) in column(s): addressline2, postalcode

### Row 2629
- Missing value(s) in column(s): addressline2, territory

### Row 2630
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2631
- Missing value(s) in column(s): addressline2, state

### Row 2632
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2633
- Missing value(s) in column(s): territory

### Row 2634
- Missing value(s) in column(s): addressline2, state
- Outlier in 'sales': 9559 (mean=3554, +/-3 std dev threshold=[-1972, 9079])

### Row 2635
- Missing value(s) in column(s): addressline2, state

### Row 2636
- Missing value(s) in column(s): addressline2, state

### Row 2637
- Missing value(s) in column(s): addressline2, territory

### Row 2638
- Missing value(s) in column(s): addressline2, territory

### Row 2639
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2640
- Missing value(s) in column(s): addressline2, state

### Row 2641
- Missing value(s) in column(s): addressline2, state

### Row 2643
- Missing value(s) in column(s): addressline2, state

### Row 2644
- Missing value(s) in column(s): addressline2, territory

### Row 2645
- Missing value(s) in column(s): addressline2, territory

### Row 2646
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2647
- Missing value(s) in column(s): addressline2, postalcode

### Row 2649
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2650
- Missing value(s) in column(s): addressline2, territory

### Row 2651
- Missing value(s) in column(s): addressline2, territory

### Row 2652
- Missing value(s) in column(s): addressline2, state

### Row 2653
- Missing value(s) in column(s): addressline2, territory

### Row 2654
- Missing value(s) in column(s): state

### Row 2655
- Missing value(s) in column(s): addressline2, territory

### Row 2656
- Missing value(s) in column(s): addressline2, territory

### Row 2657
- Missing value(s) in column(s): addressline2, state

### Row 2658
- Missing value(s) in column(s): addressline2, state

### Row 2659
- Missing value(s) in column(s): addressline2, territory

### Row 2661
- Missing value(s) in column(s): addressline2, state

### Row 2662
- Missing value(s) in column(s): addressline2, territory

### Row 2663
- Missing value(s) in column(s): addressline2, state

### Row 2664
- Missing value(s) in column(s): addressline2, territory

### Row 2665
- Missing value(s) in column(s): addressline2, state

### Row 2666
- Missing value(s) in column(s): addressline2, state

### Row 2668
- Missing value(s) in column(s): addressline2, territory

### Row 2669
- Missing value(s) in column(s): addressline2, state

### Row 2670
- Missing value(s) in column(s): addressline2, territory

### Row 2671
- Missing value(s) in column(s): addressline2, territory

### Row 2672
- Missing value(s) in column(s): addressline2, postalcode

### Row 2674
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2675
- Missing value(s) in column(s): addressline2, territory

### Row 2676
- Missing value(s) in column(s): addressline2, state

### Row 2677
- Missing value(s) in column(s): addressline2, state

### Row 2678
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2679
- Missing value(s) in column(s): addressline2, state

### Row 2680
- Missing value(s) in column(s): addressline2, territory

### Row 2681
- Missing value(s) in column(s): addressline2, postalcode

### Row 2682
- Missing value(s) in column(s): addressline2, state

### Row 2683
- Missing value(s) in column(s): addressline2, state

### Row 2684
- Missing value(s) in column(s): addressline2, territory

### Row 2686
- Missing value(s) in column(s): addressline2, state

### Row 2687
- Missing value(s) in column(s): addressline2, state

### Row 2688
- Missing value(s) in column(s): addressline2, state

### Row 2689
- Missing value(s) in column(s): addressline2, territory
- Outlier in 'quantityordered': 77 (mean=35.09, +/-3 std dev threshold=[5.868, 64.32])

### Row 2690
- Missing value(s) in column(s): addressline2, state

### Row 2691
- Missing value(s) in column(s): addressline2, state

### Row 2692
- Missing value(s) in column(s): addressline2, state

### Row 2693
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2694
- Missing value(s) in column(s): addressline2, territory

### Row 2695
- Missing value(s) in column(s): addressline2, state

### Row 2696
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2697
- Missing value(s) in column(s): addressline2, state

### Row 2698
- Missing value(s) in column(s): addressline2, territory

### Row 2699
- Missing value(s) in column(s): addressline2, state

### Row 2700
- Missing value(s) in column(s): addressline2, state

### Row 2701
- Missing value(s) in column(s): addressline2, territory

### Row 2702
- Missing value(s) in column(s): addressline2, postalcode

### Row 2703
- Missing value(s) in column(s): addressline2, territory

### Row 2704
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2705
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2706
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2707
- Missing value(s) in column(s): addressline2, territory

### Row 2708
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2709
- Missing value(s) in column(s): addressline2, state

### Row 2710
- Missing value(s) in column(s): addressline2, state

### Row 2711
- Missing value(s) in column(s): territory

### Row 2712
- Missing value(s) in column(s): addressline2, state

### Row 2713
- Missing value(s) in column(s): addressline2, state

### Row 2714
- Missing value(s) in column(s): addressline2, state

### Row 2715
- Missing value(s) in column(s): addressline2, state

### Row 2716
- Missing value(s) in column(s): addressline2, territory

### Row 2717
- Missing value(s) in column(s): addressline2, state

### Row 2718
- Missing value(s) in column(s): addressline2, state

### Row 2719
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2720
- Missing value(s) in column(s): addressline2, territory

### Row 2721
- Missing value(s) in column(s): addressline2, state

### Row 2722
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2723
- Missing value(s) in column(s): addressline2, state

### Row 2724
- Missing value(s) in column(s): addressline2, territory

### Row 2725
- Missing value(s) in column(s): addressline2, state

### Row 2726
- Missing value(s) in column(s): addressline2, state

### Row 2727
- Missing value(s) in column(s): addressline2, territory

### Row 2728
- Missing value(s) in column(s): addressline2, postalcode

### Row 2729
- Missing value(s) in column(s): addressline2, territory

### Row 2730
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2731
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2732
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2733
- Missing value(s) in column(s): addressline2, territory

### Row 2734
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2735
- Missing value(s) in column(s): addressline2, state

### Row 2736
- Missing value(s) in column(s): addressline2, state

### Row 2737
- Missing value(s) in column(s): territory

### Row 2738
- Missing value(s) in column(s): addressline2, state

### Row 2739
- Missing value(s) in column(s): addressline2, state

### Row 2740
- Missing value(s) in column(s): addressline2, state

### Row 2741
- Missing value(s) in column(s): addressline2, state

### Row 2742
- Missing value(s) in column(s): addressline2, territory

### Row 2743
- Missing value(s) in column(s): addressline2, state

### Row 2744
- Missing value(s) in column(s): addressline2, state

### Row 2745
- Missing value(s) in column(s): addressline2, territory

### Row 2746
- Missing value(s) in column(s): addressline2, territory

### Row 2747
- Missing value(s) in column(s): addressline2, state

### Row 2748
- Missing value(s) in column(s): addressline2, territory

### Row 2749
- Missing value(s) in column(s): addressline2, state

### Row 2750
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2751
- Missing value(s) in column(s): addressline2, postalcode

### Row 2752
- Missing value(s) in column(s): addressline2, territory

### Row 2753
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2754
- Missing value(s) in column(s): addressline2, territory

### Row 2755
- Missing value(s) in column(s): addressline2, state

### Row 2756
- Missing value(s) in column(s): addressline2, state

### Row 2757
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2758
- Missing value(s) in column(s): addressline2, state

### Row 2759
- Missing value(s) in column(s): addressline2, territory

### Row 2760
- Missing value(s) in column(s): addressline2, postalcode

### Row 2761
- Missing value(s) in column(s): addressline2, state

### Row 2762
- Missing value(s) in column(s): addressline2, postalcode

### Row 2763
- Missing value(s) in column(s): addressline2, territory

### Row 2765
- Missing value(s) in column(s): addressline2, state

### Row 2766
- Missing value(s) in column(s): addressline2, state

### Row 2767
- Missing value(s) in column(s): addressline2, state

### Row 2768
- Missing value(s) in column(s): addressline2, territory

### Row 2769
- Missing value(s) in column(s): addressline2, state

### Row 2770
- Missing value(s) in column(s): addressline2, state

### Row 2771
- Missing value(s) in column(s): addressline2, state

### Row 2772
- Missing value(s) in column(s): addressline2, territory

### Row 2773
- Missing value(s) in column(s): addressline2, territory

### Row 2774
- Missing value(s) in column(s): addressline2, state

### Row 2775
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2776
- Missing value(s) in column(s): addressline2, state

### Row 2777
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2778
- Missing value(s) in column(s): addressline2, state

### Row 2779
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2780
- Missing value(s) in column(s): addressline2, territory

### Row 2781
- Missing value(s) in column(s): addressline2, territory

### Row 2782
- Missing value(s) in column(s): addressline2, state

### Row 2783
- Missing value(s) in column(s): addressline2, territory

### Row 2784
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2785
- Missing value(s) in column(s): addressline2, state

### Row 2786
- Missing value(s) in column(s): addressline2, territory

### Row 2787
- Missing value(s) in column(s): addressline2, postalcode

### Row 2788
- Missing value(s) in column(s): addressline2, territory

### Row 2789
- Missing value(s) in column(s): addressline2, postalcode

### Row 2790
- Missing value(s) in column(s): addressline2, territory

### Row 2792
- Missing value(s) in column(s): addressline2, state

### Row 2793
- Missing value(s) in column(s): addressline2, state

### Row 2794
- Missing value(s) in column(s): addressline2, state

### Row 2795
- Missing value(s) in column(s): addressline2, territory

### Row 2796
- Missing value(s) in column(s): addressline2

### Row 2797
- Missing value(s) in column(s): addressline2, state

### Row 2798
- Missing value(s) in column(s): addressline2, state

### Row 2799
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2800
- Missing value(s) in column(s): addressline2, territory

### Row 2801
- Missing value(s) in column(s): addressline2, state

### Row 2802
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2803
- Missing value(s) in column(s): addressline2, state

### Row 2804
- Missing value(s) in column(s): addressline2, territory

### Row 2805
- Missing value(s) in column(s): addressline2, state

### Row 2806
- Missing value(s) in column(s): addressline2, state

### Row 2807
- Missing value(s) in column(s): addressline2, territory

### Row 2808
- Missing value(s) in column(s): addressline2, postalcode

### Row 2809
- Missing value(s) in column(s): addressline2, territory

### Row 2810
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2811
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2812
- Missing value(s) in column(s): addressline2, postalcode, territory

### Row 2813
- Missing value(s) in column(s): addressline2, state

### Row 2814
- Missing value(s) in column(s): addressline2, state, postalcode

### Row 2815
- Missing value(s) in column(s): addressline2, state

### Row 2816
- Missing value(s) in column(s): addressline2, state

### Row 2817
- Missing value(s) in column(s): territory

### Row 2818
- Missing value(s) in column(s): addressline2, state

### Row 2819
- Missing value(s) in column(s): addressline2, state

### Row 2820
- Missing value(s) in column(s): addressline2, state

### Row 2821
- Missing value(s) in column(s): addressline2, state

### Row 2822
- Missing value(s) in column(s): addressline2, territory

