def find_max(scores):
    biggest = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > biggest:
            biggest = scores[i]
    return biggest


def load_scores(path):
    kept = []
    skipped = []

    # Let open() raise FileNotFoundError unchanged.
    with open(path, "r", encoding="utf-8") as file:
        next(file, None)  # Skip the header; an empty/header-only file is valid.
        for line_number, original_line in enumerate(file, start=2):
            fields = original_line.rstrip("\r\n").split(",")
            if len(fields) != 2:
                skipped.append((line_number, original_line, "열 개수가 2가 아닙니다"))
                continue

            name, score_text = fields
            name = name.strip()
            score_text = score_text.strip()
            if not score_text:
                skipped.append((line_number, original_line, "점수가 비어 있습니다"))
                continue

            try:
                score = int(score_text)
            except ValueError:
                skipped.append((line_number, original_line, "점수가 정수가 아닙니다"))
                continue

            if not 0 <= score <= 100:
                skipped.append((line_number, original_line, "점수가 0~100 범위가 아닙니다"))
                continue
            if not name:
                skipped.append((line_number, original_line, "이름이 비어 있습니다"))
                continue

            kept.append((name, score))

    return kept, skipped