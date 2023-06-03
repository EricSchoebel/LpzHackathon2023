# Projekt zum Leipzig Open Data Hackathon 2023
## Thema: Künstliche Intelligenz für die Stadtentwicklung
### MIRA - das KI-Analysetool für die Stadt Leipzig

von Eric Schöbel

Das vorliegende Projekt entstand im Rahmen des Leipziger Open Data Hackathons 2023. Im Zuge des vom Amt für Statistik und Wahlen der Stadt Leipzig initiierten Aufrufs wurde das Thema 1: "Künstliche Intelligenz für die Stadtentwicklung" gewählt.

Entwickelt wurde *"MIRA"* (japanisch für "Spiegel"), ein *KI-Analysetool für die Stadt Leipzig*. Auf Basis von Machine-Learning-Algorithmen aus dem Bereich Unsupervised Learning können reale, öffentlich verfügbare Daten für das Stadtgebiet Leipzig aus dem Jahr 2021 live durch den Nutzer ausgewertet werden. Das als Webanwendung konzipierte Programm bietet Features zu deskriptivem Wertevergleich, Clustering und Anomalieerkennung. 

**Features**

Im Allgemeinen wird als Grundlage ein Datensatz aus dem Jahr 2021 erstellt, bei dem sich Informationen zu den 63 Leipziger Ortsteilen bezüglich 12 Kategorien, wie bspw. der Anzahl an Elektroautos oder die Anzahl der begangenen Straftaten, darlegen. Der Nutzer kann die für ihn relevanten Ortsteile und Kategorien auf der Website auswählen und nach Belieben analysieren. Datengrundlage bildete das Leipziger Informationssystem.

1. Wertevergleich

Unter "Wertevergleich" können gewählte Ortsteile hinsichtlich gewählter Kategorien in einem Balkendiagramm graphisch veranschaulicht werden. Dieses einführende Feature dient dem Zweck, sich einen Überblick über die Daten zu verschaffen und deskriptive Vergleiche ziehen zu können.

2. Clustering

Unter "Clustering" kann analysiert werden, wo sich Ortsteile gemäß gewissen Kategorien zu Gruppen ähnlicher Punkte ballen. Die Anzahl der Cluster kann selbst gewählt oder vom Programm optimiert werden. Das Ergebnis kann farblich gekennzeichnet graphisch veranschaulicht werden, insofern zwei Kategorien ausgewählt wurden. Andernfalls erfolgt eine textliche Ausgabe. Der zugrunde liegende Clustering-Algorithmus ist K-Means aus dem Bereich der Partitionierenden Clusteranalyse.

3. Anomalieerkennung

Unter "Anomalieerkennung" können Ausreißer in den Daten algorithmisch identifiziert werden. Wie zuvor können Ortsteile und Kategorien gewählt werden, für erstere muss die Anzahl mindestens 4 betragen. Für den Fall von zwei Kategorien kann das Ergebnis wieder graphisch veranschaulicht werden. Der zugrunde liegende Algorithmus ist Local Outlier Factor (LOF) aus dem Bereich der Anomaly Detection.

**Technisches**

Das *Backend* wurde in Python mithilfe von Flask entwickelt. Neben der Vorbereitung des Datensatzes werden hier insbesondere die Machine-Learning-Algorithmen der Scikit-learn Bibliothek ausgeführt. Über eine API wird das Ergebnis dem Frontend zur Verfügung gestellt. Für das *Frontend* wurde Vue.js 3 mit Vuetify 3 verwendet.

Zum Starten des Programms im Backend den Server über Ausführen von flask.py starten. Dann im Terminal in den Frontend-Ordner wechseln und über "npm run serve" das Frontend ausführen.



