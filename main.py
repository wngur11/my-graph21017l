# =========================================================
# 그래프 2
# =========================================================

st.divider()

st.header("📊 그래프 2. 일관객 합계 상위 5편의 날짜별 변화")

# 영화별 이 기간 일관객 합계 계산
top5_movies = (
    df.groupby("영화명")["일관객"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .index
    .tolist()
)

# 상위 5편만 추출
top5_df = df[df["영화명"].isin(top5_movies)].copy()

# 날짜와 영화명 순서로 정렬
top5_df = top5_df.sort_values(["날짜", "영화명"])

# 날짜별 일관객을 선 그래프로 표시
fig2 = px.line(
    top5_df,
    x="날짜",
    y="일관객",
    color="영화명",
    markers=True,
    title="일관객 합계가 가장 큰 5편의 날짜별 일관객",
    labels={
        "날짜": "날짜",
        "일관객": "일관객 수",
        "영화명": "영화"
    }
)

# 마우스를 올렸을 때 날짜와 관객수가 보이도록 설정
fig2.update_traces(
    hovertemplate=(
        "영화: %{fullData.name}<br>"
        "날짜: %{x|%Y-%m-%d}<br>"
        "일관객: %{y:,}명"
        "<extra></extra>"
    )
)

fig2.update_layout(
    hovermode="closest",
    xaxis_title="날짜",
    yaxis_title="일관객 수(명)",
    legend_title="영화"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# 그래프 설명을 직접 작성할 자리
st.subheader("📝 이 그래프로 알 수 있는 것")
st.info("여기에 이 그래프로 알 수 있는 내용을 직접 작성하세요.")
