import csv

MIN_SCORE = 0
MAX_SCORE = 100


def load_scores(path):
    """성적 CSV를 읽어 (유효한 목록, 건너뛴 줄 기록)을 돌려준다."""
    kept = []
    skipped = []

    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        for line_no, row in enumerate(reader, start=1):
            if line_no == 1:  # 헤더
                continue
            if not row:  # 빈 줄은 기록하지 않음
                continue

            original = ",".join(row)

            if len(row) != 2:
                skipped.append((line_no, original, "열 개수가 2가 아님"))
                continue

            name = row[0].strip()
            raw = row[1].strip()

            if name == "":
                skipped.append((line_no, original, "이름이 비어 있음"))
                continue
            if raw == "":
                skipped.append((line_no, original, "점수가 비어 있음"))
                continue

            try:
                score = int(raw)
            except ValueError:
                skipped.append((line_no, original, "점수가 정수가 아님"))
                continue

            if score < MIN_SCORE or score > MAX_SCORE:
                skipped.append((line_no, original, "점수가 0~100 밖"))
                continue

            kept.append((name, score))

    return kept, skipped