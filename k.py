  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::yourbucketnamehere",
                "arn:aws:s3:::yourbucketnamehere/*"
            ],
            "Effect": "Allow",
            "Principal": "*"
        }
    ]
}
