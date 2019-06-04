#### plotig regressions in season 

plt.rcParams['font.size'] = 55
plt.figure(figsize=[80,50])
plt.rcParams['savefig.dpi'] = 100
plt.rcParams['lines.linewidth'] = 6

ssp = 1000 ## size of the makar


plt.subplot(1,1,1)

X = var_x
Y =  var_y
(r, p) = stats.pearsonr(X, Y)
mask = ~np.isnan(X) & ~np.isnan(Y)
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(X[mask],Y[mask])
predict_y = slope * X + intercept

ax = sns.regplot(x=X, y=Y, color="royalblue",line_kws={'label':'$y=%3.7s*x+%3.7s$'%(slope, intercept)},scatter_kws={"s": ssp})
# plt.xlabel('Temp ($^o$C)')
ax.legend()
plt.title('title' + " r = {:.2f}".format(r) + " p = {:.3f}".format(p))
