-- Find the average marks for every subject.
SELECT subject, AVG(marks) AS average_marks
FROM Marks
GROUP BY subject
ORDER BY subject;
