package ca.kestrel.ocr

data class Fields(val amountCents: Long?, val date: String?, val merchant: String?)

interface ReceiptReader { fun read(jpeg: ByteArray): Fields }
